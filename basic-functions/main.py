#--------------------------------what is python--------------------------------------------
#____________________________________________________________________________________________________________________________
#--------------------------------Types of statements----------------------------------------
# 1.Sequentional 
# 2.loop 
# 3.selection
#____________________________________________________________________________________________________________________________
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
#____________________________________________________________________________________________________________________________
#----------------------------what is variable----------------------------------
# A temprory space in the ram to hold the data.
# Rules:
# must start with letter or in somecases Underscore _
# Must consist of letters,numbers and underscores
# Case senstive.    
# for your own remembrance ues the name of the variables that are good to remember for the humans.
#Example
#_____________________________________________________________________________________________________________________________
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
#_____________________________________________________________________________________________________________
#---------------------------------------What are data types in Python------------------------
#The type of the variable is called the data type in the python.
#Following are some of the data types and there usage with example given.
#--------------------------------------------------------------------------------------------
# Category |Type Name	       | Description & Core Purpose	| Example syntax	| Mutability
#--------------------------------------------------------------------------------------------
# Text	   |str	               | Unicode text characters	|   "Hello World"	| Immutable
#--------------------------------------------------------------------------------------------
# Numeric  |int                | Unlimited whole numbers    |    42             | Immutable                
#          |float              | Decimals / fractional value|    3.1415         | Immutable 
#          |complex	           |Real + imaginary numbers (j)|    v2 + 4j        | Immutable  
# -------------------------------------------------------------------------------------------  
#          |                   |
# Sequence |list               |Ordered, flexible collections| [1, 2, 3]        | *Mutable
#          |tuple              |Ordered, fixed collections   | (1, 2, 3)        | Immutable
#          |range              |Immutable series of numbers  | range(0, 10)     | Immutable
#---------------------------------------------------------------------------------------------
# Mapping  |dict	           | Key-value pairs	         |  {"id": 101}	    | *Mutable     
#--------------------------------------------------------------------------------------------
# Set      |set                | Unordered unique elements   |    {"a", "b"}    | *Mutable                
#          |frozenset          | Immutable version of a set  | frozenset({1, 2})| Immutable 
#---------------------------------------------------------------------------------------------
# Boolean  |bool	           | Evaluates truth values	     |  True or False	| Immutable     
#--------------------------------------------------------------------------------------------
# Special  |NoneType	       | Signifies absence of value / null|  None	    |Immutable    
#-------------------------------------------------------------------------------------------- 
# How we can check the Type? There is a buitin function in the python to check it type() e.g. type(x) .
# We can also convert the type of the variable by simply puttintg the value put in the funcation like float(x)
# • Immutable Types: 
#    Once created, their internal contents cannot be altered in place.
#    Modifying a str or an int actually creates a brand-new object in memory.
# • Mutable Types: 
#    Their data can be updated dynamically without shifting or re-allocating the object's identity 
#    pointer (e.g., adding an item to a list or changing a value in a dict).
# •Type Casting:
#    To convert a type (Casting): Use constructor functions to force a data type shift
#     float_num = float("3.14")   Converts str to float
#     int_num = int(5.99)         Truncates float to int (yields 5)
#_____________________________________________________________________________________________________________
#-----------------------------------------Input function--------------------------------------------
# The simple input function is a funtion that allows the user to enter the data to the program
# we can use the input() funtion to get the value from the user.
# Example: 
# name= input('What is your name?')
# This function returns a string value.
#Example 2: this will cause an error.
# x=input('what will be the first value?')
# y=input('what will be the seciond value?')
# z= x/y
# print(type(z),z)
# Error:TypeError: unsupported operand type(s) for /: 'str' and 'str'
# Solution: Convert it using type casting like this int
#Program that will calculate the total millage of the vehicle.
#To get the old millage of the vehicle.
# old_millage=int(input('Please Enter the old millage.'))
# current_millage=int(input('Please Enter the current millage'))
# print(type(current_millage))
# total_running=current_millage-old_millage
# print('The car run so far',total_running)
#_______________________________________________________________________________________________________________________________
#--------------------------------------------------------Conditional Statements-------------------------------------------------
#if:
#elif:
#else:
#  .




# float_num = float("3.14")  
# int_num = int(5.99)         
# print(int_num)

# x=input('what will be the first value?')
# y=input('what will be the seciond value?')
# z= x/y
# print(type(z),z)

# x= "3" 
# x=int(x)
# print(type(x))
# # x+=3
# print(x)

# y= 6
# y= x-y
# if y>3:
#     print(y)
# else:
#     print("Pakistan is working",y)