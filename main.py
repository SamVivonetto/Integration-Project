# Samuel Vivonetto
# This paticular sprint is just a run-down of what I have learned so far :P

#Hello there! welcome to my integration project! Here's a little greeting!
print("Greetings, Welcome to my project!")
print("Today you will see what I've been up to.")
print("This is just a basic guide of what I have learned so far about Python!")
print("This could also be used as a study guide for future exams or quizzes?")

#In python there are ways to tell what class a value is, using type():
print(type(34))
print(type(54.0))
print(type("Sam"))
#the first line is an integer, which outputs:<class 'int'>
#the second is a float-point which has a decimal, which outputs:<class 'float'>
#the third has quotes which makes the value a string literal: <class 'str'>
print(type("34"))
print(type("54.0"))
#Even though the two lines aboive are numbers, the quotes makes them a string!
#you are also able to change the class of a value by adding a type:
print(int(5.678))
#even thought the number inside the () is a float-point, 
#the int() only takes the integer portion



#Python can do simple arithmetic operations using standard mathematical symbols:

#Addition'+':
print(1 + 1)
#Subtraction'-':
print(2 - 1)
#Multiplication'*':
print(2 * 2)
#Exponentiation'**':
print(3 ** 2)
#Division'/':
print(8 / 2)
#Floor division'//': outputs the number that is rounded down from dividing
print(20 // 2.6)
#Modulus'%': outputs the remainder of a division
print(16 % 5)
#Python also follows the order of operations; PEMDAS
#This means any order of arithmetic will be calculated accordingly:
print(1 + 54 / 2 ** 3)

#Two operators:'+' and '*' can be used on strings also:
#'+': this operator 'concatenates' strings together: 
print('Sam' + ' is ' + 'awesome' + '!')
#'*': this operater will output the string as many times as indicated:
print("Gimme that A! " * 10)


#using '=' we can assign values to variables
#In some cases you may need to assign a number to a string:
shoeSize = "12"
#You can even assign a string to another string:
shoeColor = "green"
shoeBrand = "Nike"
#These can be input into a string to make a sentence!
print("I just bought a pair of " + shoeColor + " " + shoeBrand + " " + "shoes") 


#we can combine variables and operators to do more complex sentences:
#If a program requires user input use: input() with a question in () 
currentYear = int(input("What year is it now?: "))
birthYear= int(input("What year were you born?: "))                    
#we must use int(input()) as python can't subtract strings 
age = currentYear - birthYear
print("You are", age, "years young!!")



#There are a couple of ways to format lines of code in Python,,,

#There is a way you can write mulitiple lines in one print statement:
print("First line \n Second line")
#using '\n' you can output a new line within one line of code:
#A more practical use could be a poem:
print("''On the night's Plutonian shore!'' \n Quoth the Raven, ''Nevermore.''")

#Using 'end=' I can make any statement end in what ever follows the equal sign:
print("My name is Sam" , end= ', ')
print("I hope I get an A" , end= '!')
#As you can see there is a comma followed by a space at the end of line one.
#In the second line the line ends with the punctuation, !

#Using 'sep=' allows us to replace the comma (which normally outputs a space):
print("1" , "2", "3", "4" , sep='/')
#another example would be:
print("1" , "2", "3", "4" , sep='-')

#There are also ways you can format decimals using format():
#the letter 'd' at the end of the format can change the number of spaces from
#the string, the amount of space is the number in front of d:
pizzaSlices = 8
print("Total number of slices: ", format(pizzaSlices, '2d'))
print("Total number of slices: ", format(pizzaSlices, '4d'))
#you can also use format() in calculations of prices
#instead of using 'd' , use '.f'
#The decimal indicates how many digits after the decimal you want
#this would be useful for things like cash registers: 
numApples = int(input("How many Apples?: "))
priceApple = 2.50
totalCost = numApples * priceApple
print("Total cost of apples: $", format(totalCost, '.2f'), sep='')
#by changing the .2 to .4 we add another two digits to the right of the decimal:
print("Total cost of apples: $", format(totalCost, '.4f'), sep='')

#so far I have covered arithmetic, variables, and some formatting techniques
#we can use all of these to write some more complex code now!
#lets say you went to the movies and want to see how much you spent in total on snacks and a ticket
#We also want to know what movie you saw and if you enjoyed the show!:
movieName = input("What movie did you see?: ")
ticketPrice = float(input("How much was your ticket?: "))
numTickets = int(input("How many tickets did you buy?: "))
snackName = input("What did you order from the counter?: ")
snackPrice = float(input("How much was one of those snacks?: "))
numSnacks = int(input("How many of those snacks did you order?: "))
totalPrice = snackPrice * numSnacks + ticketPrice * numTickets
loveOrHate = input("Did you love or hate the show?: ")
print("At the movies, you watched", movieName, "and", loveOrHate + "d", "it.", sep= ' ')
print("In total, you spent: $", format(totalPrice, '.2f'), sep= '')   
print("Those Prices are outrageous!!!")
