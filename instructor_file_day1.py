############################
#         Strings          #
############################

# Hello world!
print('Hello World!')  # Input for the print() function may be a string or a number
print(32)
print(6.4)

# Sub-strings
helloWorld = 'Hello World!'
hello = helloWorld[:5]  # From beginning of string to 5th character (non-inclusive)
world = helloWorld[6:]  # From 6th character (inclusive) to end of string
ello = helloWorld[2:5]  # From 2nd character (inclusive) to 5th character (non-inclusive)
print(hello)
print(world)
print(ello)

# CHALLENGE
# Extract 'Ypsi' from 'Ypsilanti'
city = 'Ypsilanti'
nickname = None
print(nickname)

# replace()
mellowWorld = helloWorld.replace('H', 'M')  # You can replace a single character
print(mellowWorld)
mellowWorld = mellowWorld.replace(' ', 'w ')
print(mellowWorld)
sadDespondentWorld = mellowWorld.replace('Mellow', 'Sad, Despondent')  # Or you can replace a string
print(sadDespondentWorld)

# CHALLENGE
# Replace 'Dogs' with 'Cats'
text = 'Dogs are the best'
correctedText = None
print(correctedText)

# lower() / upper() / capitalize()
sadDespondentWorld = sadDespondentWorld.lower()  # lower() will change everything to lower case
print(sadDespondentWorld)
print(sadDespondentWorld.upper())  # upper() will change everything to upper case
print(sadDespondentWorld.capitalize())
# capitalize() will change the first letter of the string to upper case
# and everything else to lower case. This includes the beginning
# of other sentences.

# CHALLENGE
# Change the abomination below to 'Capitalization is great'
internet1995 = 'cApItAlIzAtIoN IS laMe'
internet2019 = None
print(internet2019)

# count()
longText = "Here are a bunch of words, but we probably don't want all of them. What now, more words?"
wordCount = longText.count(' ') + 1  # Returns the number of times the given string is found within the base string
print(wordCount)

# CHALLENGE
# Count how many times 'to be' occurs in the quote below, regardless of capitalization
hamlet = 'To be, or not to be--that is the question'
toBeCount = None
print(toBeCount)

# find()
locationOfFistWordStartingWithB = longText.find('b')
print(locationOfFistWordStartingWithB)
# The find index is useful for setting the location of sub-strings
truncatedText = longText[locationOfFistWordStartingWithB:]
print(truncatedText)
fistWordStartingWithB = truncatedText[:truncatedText.find(' ')]
print(fistWordStartingWithB)
print(longText.find('zyx'))  # If the parameter isn't found, find() will return -1

# CHALLENGE
# Create a command that will successfully extract the second word starting with 'b'
# (regardless of case) from both strings
text1 = 'Beans, Bacon, and Beer'
text2 = 'John Boehner and his merry band of rapscallions'
secondWord1 = None
secondWord2 = None
print(secondWord1)
print(secondWord2)

# Adding strings
greenEggs = 'Green eggs'
ham = 'ham'
breakfast = greenEggs + ' and ' + ham
print(breakfast)

# CHALLENGE
# Using the "animal" and "number" variable, create a new string that says, "Billions and billions of cats"
animal = 'cats'
number = 'billions'
howManyAnimals = None
print(howManyAnimals)

# Cleaning whitespace
whiteSpaceString = '     there are some unnecessary spaces here    '
print(whiteSpaceString)
print(whiteSpaceString.strip())

# CHALLENGE
# Manipulate the variable "name" so that the first and last names in the string
# are capitalized and rearranged in phone book style (e.g. "Smith, John")
name = '    john     smith '
phoneBookEntry = None
print(phoneBookEntry)

# len()
myString = "Some sample text"
stringLength = len(myString)
print(stringLength)

# CHALLENGE
# Determine how many letters there are in the string, excluding punctuation and whitespace
sampleString = '    Lorem ipsum dolor sit amet, consectetur adipiscing elit '
letterCount = None
print(letterCount)

############################
#     Variable Types       #
############################

# There are three basic variable types
# string
stringVar = '8'
# number
numVar1 = 3.4
numVar2 = 5

# You can add integers and floats...
print(numVar1 + numVar2)
# ...but you can't add numbers and strings
print(stringVar + numVar2)

# You can, however, "cast" one variable type into another
print(stringVar + str(numVar1))
print(int(stringVar) + numVar1)

# You can also print variables of different types using a print() with multiple parameters
# This will automatically add a space between each of the parameters
print(stringVar, numVar1, numVar2)

# If you don't want a space or a different delimiter, you can use the following constructions
print(stringVar, numVar1, numVar2, sep='')
print(stringVar, numVar1, numVar2, sep=', ')

# CHALLENGE
# Modify "fruitCount" to display the total number of apples + oranges
apples = 10
oranges = 5.5
fruitCount = 'I have x fruits'
print(fruitCount)

# You can assign the value of one variable to another variable, regardless of type
val = "nine"
intVal = 9
print(val)
val = intVal
print(val)
# But changing "intVal" won't change "val"
# This is because the assignment occurs "by value" as opposed to "by reference"
intVal = 22
print(val)

############################
#     Operator Types       #
############################

# + -- addition
# - -- subtraction
# * -- multiplication
# / -- division
# ** -- exponent
# % -- modulus -- Gives the remainder after division (e.g. 18 % 5 equals 3)
# // -- floor division -- Division, then rounded down (for negative numbers, toward negative infinity)
# +=, -=, *=, /=, //= -- Compound operators (e.g. x += 1 is equivalent to x = x + 1)

# The modulus (or "modulo") operator is handy for finding even and odd numbers
a = 13
b = 16
remainderA = a % 2
remainderB = b % 2
print(remainderA)
print(remainderB)

############################
#      Data Structures     #
############################

# Lists

# A variable can be a single value, but it can also be a collection of values
# An ordered collection is called a list
emptyList = []  # This initializes an empty list that can be added to later
stringList = ['hello', 'world']
floatList = [6.5, 7.8, 9.2]
mixedList = [4.5, 'words', 5, 'more words']
listOfLists = [['kittens', 'puppies', 'baby marmots'], [38, 2, 9]]

# You can access the entire list
print(listOfLists)
# A single element in the list
print(listOfLists[0])
print(listOfLists[1])
# Or, in the case of nested lists, elements within elements
print(listOfLists[0][1], listOfLists[1][1], sep=' = ')

# Values can be appended to the end of a list
print(stringList)
stringList.append('cheerio!')
print(stringList)
# They can also be inserted into the middle of a list
stringList.insert(2, 'tea and crumpets')
print(stringList)
# And values can be removed from the end of the list or any arbitrary location using .pop()
stringList.pop()
print(stringList)
stringList.pop(1)
print(stringList)

# CHALLENGE
# Add each of the tools to "toolList" using the .append() command
tool1 = '3D printer'
tool2 = 'laser cutter'
tool3 = 'bobby pin'
toolList = []
print(toolList)
# Change "tool2" to 'sawzall', then print the toolList again. What do you notice?


# Sets

# Unlike a list, a set is an UNORDERED collection of elements and there may be NO duplicate items in a set
# A set in Python is identical to a mathematical set and has operations like, union, intersection, subset, etc.
farmAnimals = {'horse', 'pig', 'sheep', 'cow', 'goat', 'dog', 'cat'}
housePets = {'fish', 'gerbil', 'dog', 'cat', 'rabbit'}
racingAnimals = {'horse', 'dog', 'gerbil'}
tastyAnimals = {'pig', 'sheep', 'cow', 'goat', 'fish'}
tastyMammals = {'pig', 'sheep', 'cow', 'goat'}

housePetsYouCanFindOnAFarm = farmAnimals.intersection(housePets)
print(housePetsYouCanFindOnAFarm)
allAnimals = racingAnimals.union(housePets).union(farmAnimals)
print(allAnimals)
areAllTastyAnimalsFoundOnFarms = tastyAnimals.issubset(farmAnimals)
print(areAllTastyAnimalsFoundOnFarms)
areAllTastyMammalsFoundOnFarms = tastyMammals.issubset(farmAnimals)
print(areAllTastyMammalsFoundOnFarms)

housePets.add('snake')
print(housePets)

# CHALLENGE
# Determine which recipes can be made from the set "ingredients" and add them to a new list
ingredients = {'chocolate', 'chicken', 'flour', 'butter', 'carrots', 'eggs', 'sugar', 'pepper'}
cake = {'chocolate', 'flour', 'butter', 'eggs', 'sugar'}
roastChicken = {'chicken', 'butter', 'salt', 'pepper'}
glazedCarrots = {'carrots', 'sugar', 'butter'}
# Add code here
listOfValidRecipes = []
print(listOfValidRecipes)

# Dictionaries

# Dictionaries are a collection of "key" and "value" pairs
myDictionary = {
    'kittens': 38,
    'puppies': 2,
    'baby marmots': 9
}

# The entire dictionary can be printed
print(myDictionary)

# You can check to see if a certain key exists in your dictionary...
print('kittens' in myDictionary)

# Get values in your dictionary by key
print(myDictionary.get('puppies'))

# ...update entries...
myDictionary['puppies'] = 0
print(myDictionary.get('puppies'))

# ...add entries...
myDictionary['ducklings'] = 12
print(myDictionary)

# ...remove entries
del myDictionary['puppies']
print(myDictionary)

# CHALLENGE
# Use the dictionary of state abbreviations to change "Lansing, Michigan" to "Lansing, MI"
states = {
    'California': 'CA',
    'Michigan': 'MI',
    'Wisconsin': 'WI',
    'Oklahoma': 'OK',
    'Florida': 'FL'
}
stateCapital = 'Lansing, Michigan'
stateFullName = None  # Extract the state name from "stateCapital"
stateAbrv = None  # Get the abbreviation from the dictionary
# Replace "stateFullName" in "stateCapital" with "stateAbrv"
print(stateCapital)

# len() -- Again!
# Remember how you could use len() to determine the length of a string? You can also use it to determine the
# length of lists, sets and dictionaries.
print(len(floatList))     # Length of a list
print(len(allAnimals))    # Length of a set
print(len(myDictionary))  # Length of a dictionary


############################
# if/elif & Boolean Logic  #
############################

# Boolean logic operators:
# True -- Note capitalization
# False -- Note capitalization
# == -- Equal
# != -- Not equal
# > -- Greater than
# < -- Less than
# >= -- Greater than or equal to
# <= -- Less than or equal to
# and
# or

a = 22
b = 13
c = 22
d = 5

# In an if/elif/else structure, the code associated with the first boolean statement to evaluate as true
# will be executed, and if none of them evaluate as true, the "else" code will execute
if a == b:
    print("a and b are equal")
elif a < b:
    print("a is less than b")
else:
    print("a is greater than b")

# When using "elif" statements, ONLY the first boolean comparison to evaluate as true will execute,
# even if more than one is true
if a == b:
    print("a and b are equal")
elif a == c:
    print("a and c are equal")
elif b < c:
    print("b is less than c")

# If several separate "if" statements are used, code associated with all true evaluations will execute
if a == b:
    print("a and b are equal")
if a == c:
    print("a and c are equal")
if b < c:
    print("b is less than c")

# Several conditions can be strung together. Use parentheses to indicate groupings.
if a > b > c or (a == c and d < b):
    print("Complex condition satisfied!")

# CHALLENGE
# Write an if statement that will result in the longer word bring printed
word1 = "hi"
word2 = "supercalifragilisticexpialidocious"

############################
#          Loops           #
############################

# A "for" loop does something a fixed number of times
# Here, we declare a new variable "x"
for x in range(0, 10):  # range(a, b) is from a (inclusive) to b (exclusive)
    print(x)

# A "while" loop does something so long as a given condition is true
y = 1
while y < 100:
    print(y)
    y *= 2  # This is the same as y = y * 2, but with less typing

# Note that in both these cases, we ended our loop statement with a ":" and indented the contents of the loop


# "for" loops can also be used for moving through "iterable" objects like lists
myList = [5, 10, 15]
for element in myList:
    print(element)

# CHALLENGE
# Add 5 to each of the elements
numbers = [1, 5, 10, 14]
# Create a loop here
print(numbers)

# Now add 3 to every other element
# Create another loop here
print(numbers)


############################
#        Functions         #
############################

# Functions let us reuse pieces of code over and over again

# "def" indicates that we're creating a function
#
def string_contains_word(string, word):
    # Since lower() returns a string, we can then call the find() operator on that string5
    if string.lower().find(word.lower()) != -1:
        return True
    else:
        return False
    # When a function is done, the return value is what is substituted
    # in place of the function in the expression in which it was called

# Another way to think of return statements is in the context of mathematical functions. f(x) or "f of x" means
# operating on the variable x to give a new result, which is then substituted into an equation.
#       e.g. f(x) = x^2
#            y = x + f(x) = x + x^2
# In our example case, we input two parameters--the full string and the word being searched for--and then when
# the statement is evaluated, the function is replaced with a "True" or a "False" value


strings = [
    "Good night moon",
    "Good night spoon",
    "Good night crumbs from my macaroon"
]
searchWord = "macaroon"

for line in strings:  # Move sequentially through each element in "strings"
    if string_contains_word(line, searchWord):  # Pass the current line and the search word to the function
        print(line)  # If the function returns a true value, print the current line


# Encapsulation
# The concept of encapsulation is to put all code that is used for a specific task inside a function and to have no
# code related to that task outside of the function. Combined with clear function names, this creates a "black box"
# system that makes code in large projects more readable and usable. With clear function names, other programmers
# (or you in the future, when you've forgotten how you structured your code) can use your code without needing to worry
# about the code inside the function. It also means you'll be able to easily skim the structure of a large project
# and get the gist of what's going on more easily.

# CHALLENGE
# Write a function that replaces every multiple of 5 with "fizz" and every even number
# that is not a multiple of 5 with "buzz"
def fizz_buzz(input_list):
    output = []
    # Add code here
    return output


sampleList = [1, 3, 5, 8, 14, 15, 23, 29, 30, 34, 37]
sampleList = fizz_buzz(sampleList)
print(sampleList)
