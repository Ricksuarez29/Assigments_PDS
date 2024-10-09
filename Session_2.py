##Exercise 1: FizzBuzz 1. Write a FizzBuzz Function: Create a function fizzbuzz(n) that takes an integer n as a parameter. 
# 2. Implement FizzBuzz Logic: The function should print:
# "Fizz" for multiples of 3
# "Buzz" for multiples of 5
# "FizzBuzz" for multiples of both 3 and 5
# The number itself for other numbers
# 3. Call the Function: Call the function for numbers 1 to 20.

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

for i in range(1,21):
    fizzbuzz(i)

# Exercise 2: Basic Data Filtering 
#1. Create a List of Mixed Data Types: Create a list that contains a mix of integers, strings, and floats. 
#2. Filter the List: Use list comprehension to create a new list that contains only the integers from the original list.
#3. Print the New List: Output the filtered list of integers.

mixed_data= [5,10,8,'hello','ricardo',2.5,5.1,'barcelona',2]

new_list=[]
for i in mixed_data:
    if type(i) == int:
        new_list.append(i)
## way to do it shorter: new_list = [x for x in mixed_data if type(x) == int]

print(new_list)

## Exercise 3: Simple To-Do List 
# 1. Create an Empty List: Start with an empty list called todo_list. 
# 2. Define Functions:
# A function add_task(task) that adds a task to the list.
# A function show_tasks() that prints all tasks in the list.

todo_list = []
def add_task(task):
    todo_list.append(task)
def show_tasks():
    print (todo_list)

## Exercise 4: Temperature Converter
# 1. Define a Conversion Function: Write a function celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit.
# 2. Print the Result: Output the converted temperature for 22ºF, 46ºF, 51ºF and 76ºF.

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(celsius_to_fahrenheit(22))
print(celsius_to_fahrenheit(46))
print(celsius_to_fahrenheit(51))
print(celsius_to_fahrenheit(76))