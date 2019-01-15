############################
#         Strings          #
############################

# Sub-strings exercise
# Extract 'Ypsi' from 'Ypsilanti
city = 'Ypsilanti'
nickname = None
print(nickname)

# replace() exercise
# Replace 'Dogs' with 'Cats'
text = 'Dogs are the best'
correctedText = None
print(correctedText)

# lower() / upper() / capitalize() exercise
# Change the abomination below to 'Capitalization is great'
internet1995 = 'cApItAlIzAtIoN IS laMe'
internet2019 = None
print(internet2019)

# count() exercise
# Count how many times 'to be' occurs in the quote below, regardless of capitalization
hamlet = 'To be, or not to be--that is the question'
toBeCount = None
print(toBeCount)

# find() exercise
# Create a command that will successfully extract the second word starting with 'b'
# (regardless of case) from both strings
text1 = 'Beans, Bacon, and Beer'
text2 = 'John Boehner and his merry band of rapscallions'
secondWord1 = None
secondWord2 = None
print(secondWord1)
print(secondWord2)

# Adding strings exercise
# Using the "animal" and "number" variable, create a new string that says, "Billions and billions of cats"
animal = 'cats'
number = 'billions'
howManyAnimals = None
print(howManyAnimals)

# Cleaning whitespace exercise
# Manipulate the variable "name" so that the first and last names in the string
# are capitalized and rearranged in phone book style (e.g. "Smith, John")
name = '    john     smith '
phoneBookEntry = None
print(phoneBookEntry)

############################
#     Variable Types       #
############################

# Variable type exercise
# Modify "fruitCount" to display the total number of apples + oranges
apples = 10
oranges = 5.5
fruitCount = 'I have x fruits'
print(fruitCount)

############################
#      Data Structures     #
############################

# List exercise
# Initialize "toolList" using the toolVariables given
tool1 = '3D printer'
tool2 = 'laser cutter'
tool3 = 'bobby pin'
toolList = None
print(toolList)
# Change "tool2" to 'sawzall', then print the toolList again. Do you expect the printed results to change?

# Sets exercise
# Determine which recipes can be made from the set "ingredients" and add them to a new list
ingredients = {'chocolate', 'chicken', 'flour', 'butter', 'carrots', 'eggs', 'sugar', 'pepper'}
cake = {'chocolate', 'flour', 'butter', 'eggs', 'sugar'}
roastChicken = {'chicken', 'butter', 'salt', 'pepper'}
glazedCarrots = {'carrots', 'sugar', 'butter'}
# Add code here
listOfValidRecipes = []
print(listOfValidRecipes)

# Dictionary exercise
# Use the dictionary of state abbreviations and the variables below
# to change "stateCapital" from "Lansing, Michigan" to "Lansing, MI"
states = {
    'California': 'CA',
    'Michigan': 'MI',
    'Wisconsin': 'WI',
    'Oklahoma': 'OK',
    'Florida': 'FL'
}
stateCapital = 'Lansing, Michigan'
stateFullName = None  # Extract the state name from "stateCapital"
stateAbrv = None

############################
# if/elif & Boolean Logic  #
############################

# if statement exercise
# Write an if statement that will result in the longer word bring printed
word1 = "hi"
word2 = "supercalifragilisticexpialidocious"

############################
#          Loops           #
############################

# for loop exercise
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

# functions exercise
# Write a function that loops through a list and creates a new list that
# replaces every multiple of 5 with the word "fizz" and
# every even number that is not a multiple of 5 with the word "buzz"
def fizz_buzz(input_list):
    output = []
    # Add code here
    return output


sampleList = [1, 3, 5, 8, 14, 15, 23, 29, 30, 34, 37]
sampleList = fizz_buzz(sampleList)
print(sampleList)

