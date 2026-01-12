# 1. String Manipulation
txt = "The price of the book is expensive."
print("We are the so-called \"Vikings\" from the north.")
print(txt.find("price"))
print(txt.find("e", 5, 10))

# 2. Fibonacci
def fib(num):
    a, b = 0, 1
    while a < num:
        print(a, end=' ')
        a, b = b, a + b

# 3. Control Flow
def if_check():
    x = int(input("\nPlease enter an integer: "))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

# 4. For Loop
def for_loop():
    vehicle = ['car', 'auto', 'plane', 'bike']
    for v in vehicle:
        print(v, len(v))

# 5. JSON Handling
import json
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)


# Python equivalent for multiplication table
# This code generates a multiplication table for the number 8
num = 8

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}"
    )

#python equivalent for division table
# This code generates a division table for the number 8
num = 8

for i in range(1, 11):
    result = num / i
    print(f"{num} ÷ {i} = {result:.2f}")

#Python equivalent for creative names of number 8
  # Five creative names of number 8
names = ["Infinity", "Octopus", "sai", "Eightball", "Eighth Wonder"]

for name in names:
    print(name)

#Python equivalent for multiplication of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = num1 * num2

print(f"{num1} × {num2} = {result}")

#Python equivalent for division of two numbers
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

# Check for division by zero
if num2 != 0:
    result = num1 / num2
    print(f"{num1} ÷ {num2} = {result:.2f}")
else:
    print("Error: Division by zero is not allowed.")

# Python equivalent for checking if a number is prime
#int main()
import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# Python equivalent for checking if a number is greater than another
a = 7
b = 5

if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(b, "is greater than", a)
else:
    print(a, "and", b, "are equal")

# Python equivalent for printing a name
#Sure! Let’s explore a few easy and fun Python programs for kids—especially useful for a 12-year-old starting out with numbers, characters, and logic. Each program is short, beginner-friendly, and teaches a cool concept:

#🧮 1. Multiplication Table of Any Number
number = int(input("Enter a number: "))
print(f"Multiplication table of {number}")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

sum = 0
for i in range(1, 11):
    sum += i
print("Sum of numbers from 1 to 10 is:", sum)

#Python equivalent for division of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 == 0:
    print("Cannot divide by zero.")
else:
    result = num1 / num2
    print("The result of the division is:", result)

#Python equivalent for division of two numbers
def divide_nums(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero.")
        return None
    else:
        return num1 / num2

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = divide_nums(num1, num2)
if result is not None:
    print("The result of the division is:", result)

#Python equivalent for division of two numbers
def div_main(num1, num2, num3):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    product = num1 * num2 * num3
    print("The product is:", product)

    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        quotient = num1 / num2
        print("The quotient is:", quotient)
    return 0

#Python equivalent for printing numbers from 1 to 10
numbers = {1,2,3,4,5,6,7,8,9,10}
for i in numbers:
    print(i)

for i in range:
    print(i)

#Python equivalent for subtraction of two numbers using operator module
import operator

num1 = 15
num2 = 8
difference = operator.sub(num1, num2)
print("The difference is:", difference)

#Python equivalent for subtraction of two numbers using function
def subtract_numbers(num1, num2):
    return num1 - num2
#Python equivalent for subtraction of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

difference = subtract_numbers(num1, num2)
print("The difference is:", difference)

#Python equivalent for sum of two numbers
def sum_numbers(num1, num2):
    return num1 + num2
#Python equivalent for sum of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = sum_numbers(num1, num2)
print(" The sum is:", sum)