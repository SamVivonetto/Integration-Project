#In python we use the assignment operator '=' to set one input equal to another
x = 7
y = 3
#We can also set an input equal to an operation of that value and another one...
x = x + y
print(x)
#using this form of operator assigns x to result of the operation...
x += y
print(x)
#because 'x = x + y' makes x = 10, 'x += y' makes x = 13 because 10 + 3 = 13.
#this is simpler and easier to read when dealing with longer programms.
#there are many other operators for the other artithmetics that python uses...

#subtraction, x = 13
x -= y
print(x)

#multiplication, x = 10
x *= y
print(x)

#division, x = 30
x /= y
print(x)

#modulus, x = 10.0
x %= y
print(x)

#exponentiation, x = 1.0
x **= y
print(x)

#floor division, x = 1.0
x //= y
print(x)

#the final value for x is 0.0
#each time x was "operated on" the value changed for x in the next operation




#python also handles comparison operators
#these comparison operators are as follows:
a = 6
b = 3
c = 6
#greater than:
print(a > b)
#the print statement outputs true because 6 is greater than 3.

#less than:
print(b < a)
#the result is true because 3 is less than 6

#greater than or equal to:
print(a >= c)
#The result is true because a and c are equal to each other
#if c is anything higher than 6 the result would also be true,
#lower and it would be false.

#less than or equal to:
print(a <= c)
#the statement above is thrue but the is the opposite of the one above
#if a was greater than c the statement would be false,
#and if a is less than c than the statement would be true.

#when wanting to compare two inputs as equal we use '==':
print(a == c)
#the result is true because 6 is equal to 6

#we can also show when something is NOT equal using '!=':
print(a != b)
#the result is true as a and b are different values.


#We can use boolean operators in python:
#There are three we will look at for this guide:'not', 'and', 'or'

#and:
print(a > b and c > b)
#both conditions must be true for the result to be true

#or:
print(a > b or b > c)
#only one condition must be met in order to be true because its one or the other.

#not:
print(not(a > b))
#while a is greater than b, the not operator makes the output the opposite:
print(not(b > c))
#3 is not greater than 6 but the not function makes it true.

#There are loops that can be created in python:
#there are different types of loops as well

#While loops:
name = input("Enter your name: ")   #takes user input for name
x = 0   #initiates x as a variable
while(x < 20):
    print(name)
    x = x + 1   #counts up by one
#the output of this program should print the user input 20 times in a row
#the number 20 is going to determine how many times name is printed

#For loop:
name = input("Enter your name: ")
for x in range(20):
    print(name)
#the for loop is more concise than the while loop.

#functions main purpose is to combine commands into one line of code:
#for example:

import math     #allows us to use more complex mathematical proccesses 

def calculateArea(radius):  #header: def calculateArea/ parameter: radius 
    area = math.pi * radius ** 2
    print("Area of a circle with a radius of", radius, "is", format(area, ".2f"))

def main():
    radius = int(input("Enter the radius: "))
    calculateArea(radius)   #calls function

### Call to main ###
main()  #runs main() function to produce the area of the circle with user radius

#functions are very useful for when code gets longer and the different blocks
#that the functions form help make code readable and understandable.
