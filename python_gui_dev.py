#############################################################################
#Python GUI - function invoke
#############################################################################
# This code creates a simple GUI application with two input boxes and a button
# When the button is clicked, it retrieves the values from the input boxes and prints them to the console.
# It also performs basic arithmetic operations and displays the results in a message box.

# Import the necessary libraries
import math  # Import math for mathematical operations
import logging  # Import logging for logging errors
import tkinter as tk
from tkinter import messagebox  # Import messagebox for displaying output

# Create the main window
root = tk.Tk()
root.title("Quick Math Calculator")  # Set the title of the window
#root.geometry("400x300")  # Set the window size

# Create labels and input boxes
label1 = tk.Label(root, text="Enter Number 1:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Enter Number 2:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Dropdown menu for selecting an operation
label_dropdown = tk.Label(root, text="Select Operation:")
label_dropdown.grid(row=2, column=0, padx=10, pady=10)

# Options for the dropdown
#operations = ["Add", "Subtract", "Multiply", "Divide"]
operations = ["Add", "Subtract", "Multiply", "Divide", "Modulus", "Exponent", "Floor Division", "Square Root", "Cube Root", "Factorial", "Power", "Logarithm", "Sine", "Cosine", "Tangent", "Cosecant", "Secant", "Cotangent", "Absolute", "Inverse", "Square", "Cube", "Min", "Max", "Mid", "Range", "Avg", "Percentage", "Percentage Difference", "Percentage Increase", "Percentage Decrease", "Percentage Change", "Percentage of"]  # Add more operations as needed

operations.sort()  # Sort the operations alphabetically
#operations = ["Add", "Subtract", "Multiply", "Divide", "Modulus", "Exponent", "Floor Division", "Square Root", "Cube Root", "Factorial", "Power", "Logarithm", "Sine", "Cosine", "Tangent", "Cosecant", "Secant", "Cotangent", "Absolute"]  # Add more operations as needed

# Create a variable to store the selected operation
selected_operation = tk.StringVar()
selected_operation.set(operations[0])  # Default value

dropdown = tk.OptionMenu(root, selected_operation, *operations)
dropdown.grid(row=2, column=1, padx=10, pady=10)

#output label
label3 = tk.Label(root, text="Output:")
label3.grid(row=3, column=0, padx=10, pady=10)

entry3 = tk.Entry(root)
entry3.grid(row=3, column=1, padx=10, pady=10)

# Function to validate inputs
def validate_inputs(value):
    try:
        return float(value)
    except ValueError:
        messagebox.showerror("Invalid Input", f"'{value}' is not a valid number.")
        return None

# Create a button to display the input values
def display_inputs():
    try:
        # Retrieve the values from the input boxes
        value1 = validate_inputs(entry1.get())
        value2 = validate_inputs(entry2.get())
        print(f"Input 1: {value1}")
        print(f"Input 2: {value2}")
        n = add(value1, value2)
        print(f"Output: {n}")

        operation = selected_operation.get()
        
        # Perform the selected operation
        if operation == "Add":
            result = add(value1, value2)
        elif operation == "Subtract":
            result = subtract(value1, value2)
        elif operation == "Multiply":
            result = multiply(value1, value2)
        elif operation == "Divide":
            result = divide(value1, value2)
        elif operation == "Modulus":
            result = modulus(value1, value2)
        elif operation == "Exponent":
            result = exponent(value1, value2)
        elif operation == "Floor Division":
            result = floor_division(value1, value2)
        elif operation == "Square Root":
            result = square_root(value1)
        elif operation == "Cube Root":
            result = cube_root(value1)
        elif operation == "Factorial":
            result = factorial(value1)
        elif operation == "Power":
            result = power(value1, value2)
        elif operation == "Logarithm":
            result = logarithm(value1, value2)
        elif operation == "Sine":
            result = sine(value1)
        elif operation == "Cosine":
            result = cosine(value1)
        elif operation == "Tangent":
            result = tangent(value1)
        elif operation == "Cosecant":
            result = cosecant(value1)
        elif operation == "Secant":
            result = secant(value1)
        elif operation == "Cotangent":
            result = cotangent(value1)
        elif operation == "Absolute":
            result = absolute(value1)
        elif operation == "Inverse":
            result = inverse(value1)
        elif operation == "Square":
            result = square(value1)
        elif operation == "Cube":
            result = cube(value1)
        elif operation == "Min":
            result = min(value1, value2)
        elif operation == "Max":
            result = max(value1, value2)
        elif operation == "Mid":
            result = mid(value1, value2)
        elif operation == "Range":
            result = range(value1, value2)
        elif operation == "Avg":
            result = avg(value1, value2)
        elif operation == "Percentage":
            result = percentage(value1, value2)
        elif operation == "Percentage Difference":
            result = percentage_difference(value1, value2)
        elif operation == "Percentage Increase":
            result = percentage_increase(value1, value2)
        elif operation == "Percentage Decrease":
            result = percentage_decrease(value1, value2)
        elif operation == "Percentage Change":
            result = percentage_change(value1, value2)
        elif operation == "Percentage of":
            result = percentage_of(value1, value2)
        else:
            result = "Invalid Operation"
        
        # Display the result in the output box
        entry3.delete(0, tk.END) # Clear the output entry box
        entry3.insert(0, (result))  # Insert the output value into the entry box
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

    logging.basicConfig(level=logging.INFO)
    logging.info(f"Operation: {operation}, Input1: {value1}, Input2: {value2}, Result: {result}")

   # Display the values in a messagebox
    messagebox.showinfo("Input Values", f"Input 1: {value1}\nInput 2: {value2}\nOutput: {result}")
    
    # Close the main window
    #root.destroy()

# Create a button to trigger the display function
button = tk.Button(root, text="Submit", command=display_inputs)
button.grid(row=4, column=0, columnspan=2, pady=10)

# Create a button to close the window function
button = tk.Button(root, text="Close", command=root.destroy)
button.grid(row=4, column=1, columnspan=2, pady=10)

def close_window():
    root.destroy()

###########################################################################
# Function to perform basic arithmetic operations
##########################################################################
# Define the arithmetic functions
# These functions perform basic arithmetic operations
# such as addition, subtraction, multiplication, and division etc.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def modulus(x, y):
    return x % y

def exponent(x, y):
    return x ** y

def floor_division(x, y):
    return x // y

def power(x, y):
    return x ** y  

def min(x, y):
    return min(x, y)
def max(x, y):  
    return max(x, y)
def range(x, y):
    return range(x, y)

def inverse(x):
    return 1 / x

def square(x):
    return x * x

def cube(x):
    return x * x * x

def min(x, y):
    return min(x, y)

def max(x, y):
    return max(x, y)

def mid(x, y):
    return (x + y) / 2

def range(x, y):
    return range(x, y)

def avg(x, y):
    return (x + y) / 2

def percentage(x, y):
    return (x / y) * 100

def percentage_difference(x, y):
    return abs((x - y) / ((x + y) / 2)) * 100

def percentage_increase(x, y):
    return ((y - x) / x) * 100

def percentage_decrease(x, y):
    return ((x - y) / x) * 100

def percentage_change(x, y):
    return ((y - x) / x) * 100

def percentage_of(x, y):
    return (x / y) * 100

def square_root(x): 
    return x ** 0.5

def cube_root(x): 
    return x ** (1/3)

def absolute(x):  
    return abs(x)

def inverse(x):
    return 1 / x

def square(x):
    return x * x

def cube(x):
    return x * x * x

def factorial(x): 
    x = int(x)  # Ensure x is an integer
    # Check if x is a negative number
    if x < 0:
        return "Error: Factorial of negative number"
    elif x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result


def logarithm(x, base): 
    if x <= 0 or base <= 1:
        return "Error: Invalid input for logarithm"
    else:
        return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x): 
    return math.tan(math.radians(x))

def cosecant(x):        
    return 1 / math.sin(math.radians(x))

def secant(x):
    return 1 / math.cos(math.radians(x))

def cotangent(x):
    return 1 / math.tan(math.radians(x))

# Create a button to trigger the display function
# Run the application
root.mainloop()
# This code creates a simple GUI application with two input boxes and a button.
# When the button is clicked, it retrieves the values from the input boxes and prints them to the console.
