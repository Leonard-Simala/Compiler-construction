non_terminal_to_missing_construct = {}

productions = (
    "",                                     # 0
    "Main-function Function-list",          # 1
    "Function Function-list",               # 2
    "EPSILON",                              # 3
    "Function-initial Function-body",       # 4
    "Type-specifier ID",                    # 5
    "void",                                 # 6
    "char",                                 # 7
    "int",                                  # 8
    "float",                                # 9
    "( Parameter-list ) { Statement-list }",                 # 10
    "Parameter Parameter-list",             # 11
    "EPSILON",                              # 12
    "Function-initial",                     # 13
    "Statement Statement-list",             # 14
    "EPSILON",                              # 15
    "Declaration-stmt",                     # 16
    "Assign-stmt",                          # 17
    "Conditional-stmt",                     # 18
    "Return-stmt",                          # 19
    "Type-specifier ID Declaration-Id ",    # 20
    ";",                                    # 21
    ", ID Declaration-Id ",                 # 22
    "#CG_PUSH_ID ID = Expression #CG_ASSIGN #CG_CLOSE_STMT ;",  # 23
    "Term Term-op",                         # 24
    "#CG_PUSH_CONST LETTER",                               # 25
    "Factor",                               # 26
    "#CG_SAVE_OP + Expression #CG_ADDOP",   # 27
    "#CG_SAVE_OP - Expression #CG_ADDOP",   # 28
    "EPSILON",                              # 29
    "#CG_SAVE_OP * Factor #CG_MULTOP",      # 30
    "#CG_SAVE_OP / Factor #CG_MULTOP",      # 31
    "#CG_PUSH_ID ID",                       # 32
    "#CG_PUSH_CONST NUMBER",                # 33
    "#CG_PUSH_CONST DECIMAL",                              # 34
    "( Expression )",                       # 35
    "if ( Condition ) #CG_SAVE Statement-body Conditional-nest",                       # 36
    "#CG_PUSH_ID ID #CG_SAVE_OP Rel-op Expression #CG_RELOP Compound-condition",       # 37
    "Log-op Condition",                     # 38
    "EPSILON",                              # 39
    "<=",                                   # 40
    ">=",                                   # 41
    "==",                                   # 42
    "<",                                    # 43
    ">",                                    # 44
    "!=",                                   # 45
    "&&",                                   # 46
    "||",                                   # 47
    "Statement #CG_IF_ELSE",                # 48
    "{ Statement-list #CG_IF_ELSE }",       # 49
    "else #CG_ELSE Condition-body ",        # 50
    "EPSILON",                              # 51
    "Elif-stmt",                            # 52
    "Else-stmt",                            # 53
    "if ( Condition ) #CG_SAVE Statement-body else #CG_ELSE Conditional-nest",      # 54
    "EPSILON",                              # 55
    "#CG_ELSE Statement-body",              # 56
    "return Return-type #CG_RETURN_SEQ_CALLEE ;",       # 57
    "ID",                                   # 58
    "NUMBER",                               # 59
    "LETTER",                               # 60
    "Main-func-initial Function-body",      # 61
    "Type-specifier main",                  # 62
    "SYNCH",                                # 63
    "EMPTY"                                 # 64
)

productions = tuple([p.split() for p in productions])

non_terminal_to_row = {
    "Program"                          : 0,
    "Function-list"                    : 1,
    "Function"                         : 2,
    "Function-initial"                 : 3,
    "Type-specifier"                   : 4,
    "Function-body"                    : 5,
    "Parameter-list"                   : 6,
    "Parameter"                        : 7,
    "Statement-list"                   : 8,
    "Statement"                        : 9,
    "Declaration-stmt"                 : 10,
    "Declaration-Id"                   : 11,
    "Assign-stmt"                      : 12,
    "Expression"                       : 13,
    "Term"                             : 14,
    "Factor"                           : 15,
    "Term-op"                          : 16,
    "Conditional-stmt"                 : 17,
    "Condition"                        : 18,                      
    "Rel-op"                           : 19,
    "Compound-condition"               : 20,
    "Log-op"                           : 21,
    "Statement-body"                   : 22,
    "Conditional-nest"                 : 23, 
    "Condition-body"                   : 24,
    "Elif-stmt"                        : 25,
    "Else-stmt"                        : 26,
    "Return-stmt"                      : 27,
    "Return-type" 		               : 28,
    "Main-function"                    : 29,
    "Main-func-initial"                : 30
}

terminal_to_col = {
    "ID":       0,
    "void":     1,
    "char":     2,
    "int":      3,
    "float":    4,
    "(":        5,
    ")":        6,
    "{":        7,
    "}":        8,
    ";":        9,
    ",":        10,
    "=":        11,
    "+":        12,
    "-":        13,
    "*":        14,
    "/":        15,
    "if":       16,
    "<=":       17,
    ">=":       18,
    "==":       19,
    "<":        20,
    ">":        21,
    "!=":       22,
    "&&":       23,
    "||":       24,
    "else":     25,
    "return":   26,
    "main":     27,
    "NUMBER":   28,
    "LETTER":   29,
    "DECIMAL":  30,
    "$":        31
}

parsing_table = (

    # 0      1     2       3      4       5      6      7      8      9     10     11     12     13     14     15     16     17     18     19     20     21     22     23     24     25    26     27      29     29      30     31
    #ID    VOID   CHAR    INT   FLOAT     (      )      {      }      ;      ,      =      +      -      *      /     IF     <=     >=     ==      <      >     !=     &&     ||    ELSE RETURN  MAIN    NUMBER LETTER DECIMAL   $
    (64,    1,      1,     1,      1,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    64), # 0 program
    (3,     2,      2,     2,      2,     3,    64,     3,    64,     3,    64,    64,    64,    64,    64,    64,     3,    64,    64,    64,    64,    64,    64,    64,    64,    64,     3,     3,    64,     64,     64,     3), # 1 Function-list
    (64,    4,      4,     4,      4,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 2 Function
    (64,    5,      5,     5,      5,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 3 Function-initial
    (64,    6,      7,     8,      9,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 4 Type-specifier
    (63,    64,    64,    64,     64,    10,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 5 Function-body
    (64,    11,    11,    11,     11,    64,    63,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 6 Parameter-list
    (64,    13,    13,    13,     13,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 7 Parameter
    (14,    14,    14,    14,     14,    64,    64,    14,    63,    64,    64,    64,    64,    64,    64,    64,    14,    64,    64,    64,    64,    64,    64,    64,    64,    64,    14,    64,    64,     64,     64,    63), # 8 Statement-list
    (17,    16,    16,    16,     16,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    18,    64,    64,    64,    64,    64,    64,    64,    64,    64,    19,    64,    64,     64,     64,    63), # 9 Statement
    (64,    20,    20,    20,     20,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 10 Declaration-stmt
    (64,    64,    64,    64,     64,    64,    64,    64,    64,    21,    22,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 11 Declaration-id
    (23,    64,    64,    64,     64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 12 Assign-stmt
    (24,    64,    64,    64,     64,    24,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    24,     25,     24,    63), # 13 Expression
    (26,    64,    64,    64,     64,    26,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    26,     64,     26,    63), # 14 Term
    (32,    64,    64,    64,     64,    35,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    33,     64,     34,    63), # 15 Factor
    (63,    64,    64,    64,     64,    63,    63,    64,    64,    63,    64,    64,    27,    28,    30,    31,    64,    64,    64,    64,    64,    64,    64,    63,    63,    64,    64,    64,    63,     64,     63,    63), # 16 Term-op
    (64,    64,    64,    64,     64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    36,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 17 Conditional-stmt
    (37,    64,    64,    64,     64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 18 Condition  
    (64,    64,    64,    64,     64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    40,    41,    42,    43,    44,    44,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 19 Rel-op
    (64,    64,    64,    64,     64,    64,    63,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    38,    38,    64,    64,    64,    64,     64,     64,    63), # 20 Compound-condition
    (64,    64,    64,    64,     64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    46,    47,    64,    64,    64,    64,     64,     64,    63), # 21 Log-op  
    (48,    48,    48,    48,     48,    64,    64,    49,    64,    64,    64,    64,    64,    64,    64,    64,    48,    64,    64,    64,    64,    64,    64,    64,    64,    64,    48,    64,    64,     64,     64,    63), # 22 Statement-body
    (53,    53,    53,    53,     53,    64,    64,    53,    64,    64,    64,    64,    64,    64,    64,    64,    53,    64,    64,    64,    64,    64,    64,    64,    64,    50,    53,    64,    64,     64,     64,    63), # 23 Conditional-nest
    (53,    53,    53,    53,     53,    64,    64,    53,    53,    64,    64,    64,    64,    64,    64,    64,    52,    64,    64,    64,    64,    64,    64,    64,    64,    64,    53,    64,    64,     64,     64,    63), # 24 Condition-body
    (53,    64,    64,    64,     64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    54,    64,    64,    64,    64,    64,    64,    64,    64,    63,    64,    64,    64,     64,     64,    63), # 25 Elif-stmt
    (56,    56,    56,    56,     56,    64,    64,    56,    64,    64,    64,    64,    64,    64,    64,    64,    56,    64,    64,    64,    64,    64,    64,    64,    64,    56,    56,    64,    64,     64,     64,    63), # 26 Else-stmt
    (64,    64,    64,    64,     64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    57,    64,    64,     64,     64,    63), # 27 Return-stmt
    (58,    64,    64,    64,     64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    59,     59,     64,    63), # 28 Return-type
    (64,    61,    61,    61,     61,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63), # 29 Main-function
    (64,    62,    62,    62,     62,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,    64,     64,     64,    63)  # 30 Main-func-initial
)