#int data type, there are 4 ways to write an int data type
# binary, octal, decimal and hexadecimal , decimal is the default way to write an int data type
from calendar import c


x=5
bin(x) # binary
oct(x) # octal
hex(x) # hexadecimal


#float data type
a = 1.5
print(a)
#a=0B101.101 # binary float,This is not a valid syntax , float has to be represented in interger value only.
print(a)
print(a)
type(a)
b = 1.5e2 # scientific notation or exponential form
print(b)

#complex notation format
a+bj
#a is real part and b is imaginary part  and j is fixed variable j2=-1 j=sqrt(-1)
c = 2+3j
c=complex(2,3) # this is another way to write complex number
c=20j+5 # this is another way to write complex number
c=-10+20j # this is another way to write complex number
c=10.5+20.6j # this is another way to write complex number
c=0B11+20j # the integer part of the complex number can be written in binary, octal or hexadecimal format but the float part of the complex number cannot be written in binary, octal or hexadecimal format
c=10+0B101j # this is invalid syntax because the float part of the complex number cannot be written in binary, octal or hexadecimal format


#boolean data type 
#boolean values / logical values
#True and False are the boolean values in python and they are case sensitive
#boolean values are used to represent the truth value of an expression or a statement
#boolean values are used in conditional statements and loops to control the flow of the program
#boolean values are also used in comparison operators to compare two values and return a boolean value as a result
#boolean values can be represented as 1 and 0 in python, where 1 represents True and 0 represents False
#ex. comparision operators
if age > 18:
    print("You are an adult")

    True+True # this will return 2 because True is represented as 1 in python
    True+False # this will return 1 because True is represented as 1 and False is represented as 0 in python
    True*True # this will return 1 because True is represented as 1 in python
    False*True # this will return 0 because False is represented as 0 in python
    False*False # this will return 0 because False is represented as 0 in python
    True-False # this will return 1 because True is represented as 1 and False is represented as 0 in python
    True/True # this will return 1 because True is represented as 1 in python
    False+False # this will return 0 because False is represented as 0 in python

#string data type
#string is a sequence of characters enclosed in single quotes, double quotes or triple quotes
#string can be represented in single quotes, double quotes or triple quotes
#multi line string can be represented in triple quotes
#string can be concatenated using + operator
#Example of string data type
x="Hello World"
x='Hello World'
x='''Hello World'''
x="Hello " + "World" # this will concatenate the two strings and return "Hello World"
x="Hello " * 3 # this will repeat the string "Hello " three times and return "Hello Hello Hello "
#example of multi line string
x="Hello 
        World" # this will return "Hello\nWorld" because the new line character is represented as \n in python



#indexing and slicing of string
#string indexing starts from 0 and ends at n-1 where n is the length of the string
#string slicing is used to extract a portion of the string using the index values
#string slicing syntax is string[start:end:step] where start is the starting index, end is the ending index and step is the step value

s='umesh NS'
    s[0] # this will return 'u' because it is the character at index 0  s[-6] # this will return 'u' because it is the character at index -6 
    s[1] # this will return 'm' because it is the character at index 1
    s[2] # this will return 'e' because it is the character at index 2
    s[3] # this will return 's' because it is the character at index 3
    s[4] # this will return 'h' because it is the character at index 4
    s[5] # this will return ' ' because it is the character at index 5 
    s[6] # this will return 'N' because it is the character at index 6

#to calculate the length of the string we can use the len() function
x=[len(s)-1]





    




