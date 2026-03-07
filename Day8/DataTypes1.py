#Data Types

from ast import List
from ctypes import LittleEndianStructure
from curses import intrflush


Data type represents the type of data represented by a Variable. 
It defines the operations that can be performed on the data and the way it is stored in memory. 
Common data types include integers, floating-point numbers, strings, and booleans. 
Each programming language has its own set of data types, and understanding them is crucial for writing efficient and effective code.

# Example of data types in Python

int
float
complex
bool
str

List
tuple
set
dict
frozenset

bytes
bytearray
range
None

#In linux every object is treated as a file, including data types.
#This means that data types can be read from and written to files, and can be manipulated using file operations.
#In Linux, data types are also used to define the structure of files and directories, and to manage permissions and access control.
#For example, when you create a file in Linux, it is assigned a data type based on its contents, such as text or binary.
#This allows the operating system to determine how to handle the file and what applications can open it.
#In addition, Linux provides various tools and commands for working with data types, such as the 'file' command to determine the type of a file, and the 'stat' command to view the metadata of a file, including its data type.
#Overall, data types play a crucial role in Linux and are essential for managing files, directories, and permissions effectively.
#In summary, data types are fundamental to programming and are essential for managing and manipulating data effectively.
#Understanding data types is crucial for writing efficient and effective code, and is an important aspect of programming in any language.
#In Python,eerything is treated as object and data types are dynamic, meaning that the type of a variable can change during runtime.
#In contrast, in statically-typed languages like C++ and Java, the type of a variable must be declared at compile time and cannot change during runtime.
#In Linux, data types are also important for managing files and directories, as they determine how the operating system handles and interacts with them.
#In conclusion, data types are a fundamental concept in programming and are essential for managing and manipulating data effectively.

most commonly used data types in python are 
1. print(x)
2. type(x)
3. id(x) #address of x

#int data type is used to represent whole numbers, both positive and negative, without any decimal points.
#In Python, the int data type can handle arbitrarily large integers, limited only by the available memory of the system.
#Example of int data type in Python
x = 10
y = -5456455676578679789789647854765364356435645
type(x) # <class 'int'>
type(y) # <class 'int'>

#We can represent int value in different number systems such as binary, octal, and hexadecimal.
#Decimal representation of an integer is the standard base-10 representation that we use in everyday life.
#Binary representation of an integer is prefixed with '0b' or '0B'. Base 2
#Octal representation of an integer is prefixed with '0o' or '0O'. Base 8
#Hexadecimal representation of an integer is prefixed with '0x' or '0X'. Base 16
#Example of representing int value in different number systems

1. Decimal representation (base 10)
Allowed digits are 0 , 1, 2, 3, 4, 5, 6, 7, 8, 9
x = 10
print (x) # 10
type(x) # <class 'int'>

2. Binary representation (base 2)
Allowed digits are 0 and 1
The allowed digits are: 0 and 1
The number should be prefixed with '0b' or '0B' to indicate that it is a binary number.

x = 0b1010
print (x) # 10
type(x) # <class 'int'>

3. Octal representation (base 8)
Allowed digits are 0, 1, 2, 3, 4, 5, 6, and 7
The number should be prefixed with '0o' or '0O' to indicate that it is an octal number.
x = 0o12
print (x) # 10
type(x) # <class 'int'>

4. Hexadecimal representation (base 16)
Allowed digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F (or a, b, c, d, e, and f) 
The number should be prefixed with '0x' or '0X' to indicate that it is a hexadecimal number.
x = 0xA
print (x) # 10
type(x) # <class 'int'>

NOTE: 
    In Python, the int data type can handle arbitrarily large integers, so there is no limit to the size of an integer that can be represented.
    However, the amount of memory available on the system may limit the size of an integer that can be stored.
        Python automatically manages memory for integers, and will allocate more memory as needed to accommodate larger integers.
            Python considers all of the base systems (binary, octal, hexadecimal) as integers, and they are all represented using the int data type. 
                Therefore, there is no separate data type for binary, octal, or hexadecimal numbers in Python. 
                    They are all treated as integers and can be used interchangeably in calculations and operations.
