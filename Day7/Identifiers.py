#Python identifier: A name in python is called an identifier. It is used to identify a variable, function, class, module or other object. 
#An identifier starts with a letter A-Z or a-z or an underscore (_) followed by zero or more letters, underscores and digits (0-9). 
#Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case-sensitive programming language.
# Therefore, myClass and myclass are two different identifiers in Python. 

x=10
def f1(): #f1 is identifier for function
    print('f1 function')
class Test:
    def m1(self):
        print('m1 method')

cash=10 #valid
ca$h=10 #invalid as it contains $
cash_amount=10 #valid
123cash=100 #invalid as it starts with number
cash123=100 #valid as it starts with alphabet


# all of the below identifiers are different as python identifiers are case senstive

Total=10
total=20
TotAl=30

#There is no length limit to define identifier.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa=10
print (aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa)

reserved word cannot be used as identifier. For example, we cannot use 'if' as an identifier because it is a reserved word in Python.
if=10 #invalid as 'if' is a reserved word in python

_x #is protected identifier
__x #is private identifier
___x #is a special identifier used in Python for name mangling. 
#It is used to avoid name clashes in subclasses. 
#When a variable is defined with two leading underscores and no trailing underscores, 
#it is considered a private variable and is not accessible from outside the class. 
#However, it can still be accessed using name mangling by prefixing the variable name with _ClassName. 
#For example, if we have a class named Test and a private variable named __x, we can access it using _Test__x.
__x__ #is a special identifier used in Python for special methods. or magic methods. 
#These methods have a specific meaning and are used to define the behavior of objects in Python.




