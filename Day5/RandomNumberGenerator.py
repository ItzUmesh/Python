#Generate random numbers
from random import  randint
print (randint(0,9))

#To generagte more numbers

from random import randint
print (randint(0,9) , randint(0,9) )

#print always prints with space in between
print (1,2,3,4,5)

#to remove the space we can use sep parameter
print (1,2,3,4,5 ,sep='')

#to generate 10 different random numbers between 0 and 9
from random import randint
for i in range(10):
    print (randint(0,9),randint(0,9),sep='')
