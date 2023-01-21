# Compiler construction

## Description

A compiler is a software tool which transforms source code written in a specified programming language into machine code that can be executed by a computer.  

A compiler consists of the following modules:

**Lexical analyzer:** Breaks the source code into a sequence of tokens.  
**Syntax analyzer:** Checks the source code for syntax errors and builds an abstract syntax tree (AST).  
**Semantic analyzer:** Checks the source code for semantic errors and adds type information to the AST.  
**Intermediate code generator:** Translates the AST into an intermediate representation of the code.
**Code optimizer:** Improves the intermediate code for efficient execution.  
**Code generator:** Translates the optimized intermediate code into machine code.  
Some compilers have additional modules such as error reporting and debugging facilities.  

## This Repository

This Repo covers implementation of a simple compiler for a subset of the C programming language written in python implementing the following modules:  
lexical analyser  
semantic analyser  
Intermediate Code Generator  
Error checking and reporting  
Semantic analyser - not as a standalone module  

It is a simple compiler but its sophistication is in it simplicity  

## Tools

Vscode
Drawing software  
python programming language  
c programming language  
Months and monthe of resaerch and coding

## Technique

The text categories are specified with regular expressions  
The technique is to combine those into a single master regular expression
and to loop over successive matches:  

## References

official re library documentation <https://docs.python.org/3/library/re.html#:~:text=A%20regular%20expression%20(or%20RE>,down%20to%20the%20same%20thing).
