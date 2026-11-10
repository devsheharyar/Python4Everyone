#--------------------------------what is python--------------------------------------------
#--------------------------------Types of statements----------------------------------------
# 1.Sequentional 
# 2.loop 
# 3.selection
#--------------------------------reserved words--------------------------------------------
# Booleans & Null------------True, False, None
# Logical Operators	         and, or, not
# Control Flow---------------if, elif, else
# Loops & Iteration	         for, while, break, continue, in
# Functions & OOP------------def, class, lambda, return, pass
# Exception Handling	     try, except, finally, raise, assert
# Context Management---------with, as
# Modules & Scope	         import, from, global, nonlocal, del
# Asynchronous Programming---async, await
# Pattern Matching	         match, case
#----------------------------what is variable----------------------------------
# A temprory space in the ram to hold the data.
# Rules:
# must start with letter or in somecases Underscore _
# Must consist of letters,numbers and underscores
# Case senstive.    
# for your own remembrance ues the name of the variables that are good to remember for the humans.
#Example
#------------------------------What are operators--------------------------------

# ------------------------------
# | Operator |  Operation      |
# ------------------------------
# |    =     |  Assignment     |
# ------------------------------
# |   ==     |  Equal          |
# ------------------------------
# |    +     |  Addition       |
# ------------------------------
# |    -     |  Subtrction     |
# ------------------------------
# |    *     |  Multiplication |
# ------------------------------
# |    /     |  Division       |
# ------------------------------
# |    **    |  Power          |
# ------------------------------
# |    %     |  Remanider      |
# ------------------------------
# Which operator will go first (Operator Precedence)?
# 1st Parenthesis 
# 2nd Power 
# 3rd Multiplication
# 4th Addition 
# if same left to right.
#Example left to right.
# 1+8/4*5 <= in this example the 8/4 will execute first not 4*5. 
# More briefly operators operations execution written below. 
#----------------------------------------------------------
# 1. Grouping & Referencing (Highest Priority)
# • () — Parentheses
# • [] — Slicing or subscription
# • . — Attribute reference
#----------------------------------------------------------
# 2. Arithmetic: Exponents
# • ** — Exponentiation (evaluates right-to-left)
#----------------------------------------------------------
# 3. Unary Operators
# • +x, -x — Positive, Negative
# • ~x — Bitwise NOT
#----------------------------------------------------------
# 4. Arithmetic: Multiplication & Division
# • * — Multiplication
# • / — Division
# • // — Floor division
# • % — Modulo (Remainder)
#-----------------------------------------------------------
# 5. Arithmetic: Addition & Subtraction
# • + — Addition
# • - — Subtraction
#------------------------------------------------------------
# 6. Bitwise Shifts
# • <<, >> — Left and right bitwise shifts
#------------------------------------------------------------
# 7. Bitwise AND, XOR, & OR
# • & — Bitwise AND
# • ^ — Bitwise XOR
# • | — Bitwise OR
#------------------------------------------------------------
# 8. Comparisons & Membership
# • <, <=, >, >= — Relational comparisons
# • ==, != — Equality tests
# • is, is not — Object identity
# • in, not in — Membership tests
#------------------------------------------------------------
# 9. Logical NOT
# • not — Boolean NOT
#------------------------------------------------------------
# 10. Logical AND
# • and — Boolean AND
#------------------------------------------------------------
# 11. Logical OR
# • or — Boolean OR
#------------------------------------------------------------
# 12. Conditional Expressions
# • if - else — Ternary operator
#------------------------------------------------------------
# 13. Assignment (Lowest Priority)
# • =, +=, -=, *=, etc. — Assignment operators


x= 3 
x+=3
print(x)

y= 6
y= x-y
if y>3:
    print(y)
else:
    print("Pakistan is working",y)