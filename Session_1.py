## Syntax and variables

#Exercise 1: Write a Python program that prints a greeting message, such as "Hello, Python!".
print("Hello, Python!")

#Exercise 2:Create a program that: Defines two variables, a and b, with numerical values. 
#Prints their sum, difference, product, and quotient.
a = 10
b = 5
suma= a+b
difference = a-b
product = a*b
quotient = a/b
print(sum), print(difference), print(product)
print(quotient)

#Exercise 3: Define a variable name and assign it your name. Write a program that prints a message saying
# "Hello, [name]!" where [name] is the value of the variable.
name= 'Ricardo'
print(f'Hello, {name}!')

## Lists and Dictionaries

#Exercise 4:Create a list called universities with at least five different university names.Print the entire list.
#Print the first and last university in the list.

universities = ['ESADE', 'IE', 'IESE', 'Pompeu Fabra', 'UPC']
print(f"The different universities are: {', '.join(universities)}")
print(f"The first university is {universities[0]} and the last is {universities[-1]}")

#Exercise 5:Create a dictionary called student with keys: name, age, and grade, and assign appropriate values to each key.
# Write a program that prints each key-value pair in the dictionary.

students= {'name': 'Ricardo', 'age': 20, 'grade': 10}
for key, value in students.items():
    print(key, value)

##Tuples and Sets
#Exercise 6: Define a tuple called coordinates with two values representing a point in 2D space (e.g., (x, y)).
# Print the value of coordinates and access each element by its index.

coordinates = (1, 2)
print(coordinates)
print(coordinates[0], coordinates[1])

#Exercise 7: Create a set called colors with the values: "red", "green", "blue". Add another color to the set.
# Try adding a duplicate color and observe what happens. Print the set and remove one color from it.
# Create another set named light_colors and merge colors and light_colors.

colors= {'red', 'green', 'blue'}
colors.add('yellow')
colors.add('red')
print(colors)
colors.remove('yellow')
print(colors)
light_colors = {'yellow', 'light green', ''}
colors.update(light_colors)
print(colors)

##Control flow
#Exercise 8: Write a program that: Takes an input number from the user. Checks if the number is positive, negative, or zero.
# Prints an appropriate message based on the result.

number= int(input('Enter a number: '))
if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')

#Exercise 9: For Loop. Create a list of numbers from 1 to 5. Use a for loop to iterate through the list and print each number.

list_numbers=[1, 2, 3, 4, 5]
for i in list_numbers:
    print(i, end= ' ')

#Exercise 10: While Loop. Write a program that uses a while loop to print numbers from 1 to 5. Ensure the loop terminates correctly.

iterable=1
while iterable <= 5:
    print(iterable, end= ' ')
    iterable+=1

#Exercise 11: Match Statement. Write a program that: Asks the user to input a grade (e.g., "A", "B", "C", "D", or "F").
# Use a match statement to print a corresponding message for each grade: "A": "Excellent!" "B": "Good job!" "C": "Fair."
# "D": "Needs improvement." "F": "Failing." Handle invalid input by printing a default message.

grade= input('Enter a grade: ')
match grade:
    case 'A':
        print('Excellent!')
    case 'B':
        print('Good job!')
    case 'C':
        print('Fair.')
    case 'D':
        print('Needs improvement.')
    case 'F':
        print('Failing.')
    case _:
        print('Invalid grade')


##Function
# Exercise 12: Write a function called greet that takes a name as an argument and prints "Hello, [name]!".
# Call the function with your own name.

def greet(name):
    return print(f'Hello, {name}!')
greet('Ricardo')

# Exercise 13: Define a function called square that takes a number as an argument and returns its square.
# Print the result of calling this function with different numbers.
 
def square(number):
    return number**2
print(square(4))

 
# Exercise 14: Write a function called multiply that takes two parameters, a and b, and returns their product.
# Set a default value of 1 for the parameter b. Test the function with and without providing the second argument.

def multiply(a, b=1):
    return a*b
print(multiply(5, 2))
print(multiply(5))

#Exercise 15: Create a list of numbers from 1 to 10. 
# Use list comprehension to create a new list that contains the squares of these numbers. Print the new list.

list= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares= []
for i in list:
    squares.append(i**2)
print(squares)

#Exercise 16: Create a dictionary where the keys are names of students and the values are lists of their grades.
# Write a function that takes the dictionary and prints the average grade for each student.

grades= {'Ricardo':[10,9,7,8], 'Joaquin':[5,9,5,8], 'Cristian':[10,9,9,10]}

def average(grades):
    for key, value in grades.items():
        print(key, sum(value)/len(value))

average(grades)

#Exercise 17: Write a program that: Defines a function calculate which takes three parameters: two numbers and an operator (+, -, *, /).
# Performs the operation and returns the result.
# Ask the user for the two numbers and the operator, then call the function and print the result.

def calculate(a, b, operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b
    else:
        return 'Invalid operator'
num1= int(input('Enter a number: '))
num2= int(input('Enter another number: '))
oper= input('Enter an operator: ')
print(calculate(num1, num2, oper))
