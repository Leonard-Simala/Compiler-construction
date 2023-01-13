import os
from symbolTableManager import SymbolTableManager
from memory_manager import MemoryManager

script_dir = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


class CodeGen(object):
    def __init__(self):
        self.semantic_stack = []
        self.call_seq_stack = []
        self.cont_label_stack = []
        self.break_loc_stack = []

        self.semantic_routines = {
            "INIT_PROGRAM": self.init_program_routine,
            "FINISH_PROGRAM": self.finish_program_routine,
            "#CG_RETURN_SEQ_CALLEE": self.return_seq_callee_routine,
            "#CG_PUSH_ID": self.push_id_routine,
            "#CG_PUSH_CONST": self.push_const_routine,
            "#CG_CLOSE_STMT": self.close_stmt_routine,
            "#CG_ASSIGN": self.assign_routine,
            "#CG_MULTOP": self.multop_routine,
            "#CG_SAVE_OP": self.save_op_routine,
            "#CG_RELOP": self.relop_routine,
            "#CG_LOGOP": self.logop_routine,
            "#CG_ADDOP": self.addop_routine,
            "#CG_SAVE": self.save_routine,
            "#CG_IF_ELSE": self.if_else_routine,
            "#CG_ELSE": self.else_routine,
        }

        self.token_to_op = {
            "+": "ADD",
            "-": "SUB",
            "*": "MULT",
            "/": "DIV",
            "<=": "LTE",
            ">=": "GTE",
            "!=": "NE",
            "==": "EQ",
            "<": "LT",
            ">": "GT",
            "&&": "AND",
            "||": "OR"
        }

        self.program_block = []

        #self.output_file = os.path.join(os.path.dirname(script_dir), "outputs", "three_Address_code.txt")
        self.output_file = os.path.join(
            script_dir, "outputs", "three_address_codes.txt")

    @property
    def stack_frame_ptr_addr(self):
        ''' memory location for runtime stack frame pointer variable '''
        return MemoryManager.static_base_ptr

    @property
    def print_addr(self):
        return MemoryManager.static_base_ptr + 4

    @property
    def arg_counter(self):
        return [len(l) for l in SymbolTableManager.arg_list_stack]

    def _add_three_addr_code(self, three_addr_code, idx=None, insert=False, increment=True):
        if idx is None:
            idx = MemoryManager.pb_index
        if isinstance(three_addr_code, tuple):
            three_addr_code = self._get_three_addr_code(
                three_addr_code[0], *three_addr_code[1:])
        if insert:
            self.program_block[idx] = (idx, three_addr_code)
        else:
            self.program_block.append((idx, three_addr_code))
        if increment:
            MemoryManager.pb_index += 1

    def _add_placeholder(self):
        self._add_three_addr_code("PLACEHOLDER")

    def _add_print_code(self, t):
        self._add_three_addr_code(self._get_three_addr_code("print", t))

    def _get_three_addr_code(self, opcode, *args):
        three_addr_code = "(" + opcode.upper()
        for i in range(3):
            try:
                arg = args[i]
                three_addr_code = three_addr_code + ", " + str(arg)
            except IndexError:
                three_addr_code = three_addr_code + ", "
        return three_addr_code + ")"

    def _get_context_info(self):
        scope_stack = SymbolTableManager.scope_stack
        symbol_table = SymbolTableManager.symbol_table
        return scope_stack, symbol_table

    def _get_enclosing_fun(self, level=1):
        try:
            scope_stack = SymbolTableManager.scope_stack
            symbol_table = SymbolTableManager.symbol_table
            return symbol_table[scope_stack[-level] - 1]
        except IndexError:
            return None

    def _get_add_code(self, *args):
        return self._get_three_addr_code("ADD", *args)

    def _get_sub_code(self, *args):
        return self._get_three_addr_code("SUB", *args)

    def _get_static_addr(self, offset):
        return MemoryManager.static_base_ptr + offset

    def _resolve_addr(self, operand):
        if isinstance(operand, int):
            addr = operand
        elif "address" in operand:
            addr = operand["address"]  # static address
        else:
            print("the stuff")
            print(operand)
            # need to calculate dynamic address

            t_arg_addr = MemoryManager.get_temp()
            print(t_arg_addr)
            print(self.stack_frame_ptr_addr)
            v = MemoryManager.get_static()
            print(v)
            # print(f"#{operand['offset']}")

            self._add_three_addr_code(self._get_add_code(self.stack_frame_ptr_addr, v, t_arg_addr))
            addr = f"@{t_arg_addr}"
        return addr

    def save_output(self):
        with open(self.output_file, "w") as f:
            if self.program_block:
                for lineno, three_addr_code in self.program_block:
                    f.write(f"{lineno}\t{three_addr_code}\n")
            else:
                f.write("Failed to generate output program.\n")

    ''' semantic routines begin here '''

    def push_const_routine(self, input_token):
        addr = MemoryManager.get_static()
        const = "#" + input_token[1]
        self._add_three_addr_code(
            self._get_three_addr_code("assign", const, addr))
        self.semantic_stack.append(addr)

    def push_id_routine(self, input_token):
        id_row = SymbolTableManager.symbol_table[input_token[1]]
        self.semantic_stack.append(id_row)

    def init_program_routine(self, input_token):
        three_addr_code = self._get_three_addr_code("assign", f"#{MemoryManager.stack_base_ptr}",
                                                    self.stack_frame_ptr_addr)
        self._add_three_addr_code(three_addr_code)
        # allocate space for stack ptr and print address (+0 and +4)
        MemoryManager.static_offset += 8
        for _ in range(3):
            self._add_placeholder()

    def assign_routine(self, input_token):
        try:
            A = self._resolve_addr(self.semantic_stack.pop())
            R = self._resolve_addr(self.semantic_stack[-1])
            self._add_three_addr_code(("assign", A, R))
        except IndexError:
            pass

    def save_op_routine(self, input_token):
        op = self.token_to_op[input_token[1]]
        self.semantic_stack.append(op)

    def multop_routine(self, input_token):
        try:
            op = self.semantic_stack.pop(-2)
            self.binary_op_routine(op)
        except IndexError:
            pass

    def relop_routine(self, input_token):
        try:
            op = self.semantic_stack.pop(-2)
            self.binary_op_routine(op)
        except IndexError:
            pass

    def logop_routine(self, input_token):
        try:
            op = self.semantic_stack.pop(-2)
            self.binary_op_routine(op)
        except IndexError:
            pass

    def addop_routine(self, input_token):
        try:
            op = self.semantic_stack.pop(-2)
            self.binary_op_routine(op)
        except IndexError:
            pass

    def binary_op_routine(self, op):
        try:
            R = MemoryManager.get_temp()
            A2 = self._resolve_addr(self.semantic_stack.pop())
            A1 = self._resolve_addr(self.semantic_stack.pop())
            self._add_three_addr_code((op, A1, A2, R))
            self.semantic_stack.append(R)
        except IndexError:
            pass

    def finish_program_routine(self, input_token):
        # back patch main jump here
        t_ret_addr = MemoryManager.get_temp()
        # self.program_block[1] = (1, self._get_sub_code(
        #     self.stack_frame_ptr_addr, "#4", t_ret_addr))
        # self.program_block[2] = (2, self._get_three_addr_code(
        #     "assign", f"#{MemoryManager.pb_index}", f"@{t_ret_addr}"))
        # self.program_block[3] = (3, self._get_three_addr_code(
        #     "jp", SymbolTableManager.findrow("main")["address"]))

    def return_seq_callee_routine(self, input_token):
        t = MemoryManager.get_temp()
        # save return address into temp variable
        self._add_three_addr_code(self._get_sub_code(
            self.stack_frame_ptr_addr, "#4", t))
        t2 = MemoryManager.get_temp()
        self._add_three_addr_code(
            self._get_three_addr_code("assign", f"@{t}", t2))
        self._add_three_addr_code(self._get_three_addr_code("jp", f"@{t2}"))

    def close_stmt_routine(self, input_token):
        if self.semantic_stack:
            self.semantic_stack.pop()  # pop result of last assignment

    def save_routine(self, input_token):
        self.semantic_stack.append(MemoryManager.pb_index)
        self._add_placeholder()

    def if_else_routine(self, input_token):
        try:
            saved_idx = self.semantic_stack.pop()
            self._add_three_addr_code(("jp", MemoryManager.pb_index),
                                      idx=saved_idx, insert=True, increment=False)
        except IndexError:
            pass

    def else_routine(self, input_token):
        try:
            saved_idx = self.semantic_stack.pop()
            cond = self._resolve_addr(self.semantic_stack.pop())
            self.semantic_stack.append(MemoryManager.pb_index)
            self._add_placeholder()
            self._add_three_addr_code(("jpf", cond, MemoryManager.pb_index),
                                      idx=saved_idx, insert=True, increment=False)
        except IndexError:
            pass

    ''' Semantic routines end here '''

    def code_gen(self, action_symbol, input_token):
        if SymbolTableManager.error_flag:
            try:
                self.semantic_routines[action_symbol](input_token)
            except Exception as e:
                print(f"Error in semantic routine {action_symbol}:", str(e))
