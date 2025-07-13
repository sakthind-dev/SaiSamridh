######################################################################################
#########################python Learnings
######################################################################################

import pandas as pd
  
#helloworld
print('hello world')

#version
import sys
print(sys.version)

import random
      
#indentation - Python uses indentation to indicate a block of code. 	 	
if 5 > 2:
        print("Five is greater than two!")
if 5 < 2:
	print("Five is greater than two!")
else:
        print("Two is leser than Five!")

"""
Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""
x = "awesome"

def myfunc():
	global x1
	x = "fantastic"
	x1 = x
	print("Python is " + x)

def func_var():
        #variables
        x = 5
        y = "Hello, World!"

        #TODO - sakthi -to test sonarlint
        #FIXME
        #This is a comment - Multiline #FIXME
        #written in
        #more than just one line
        print(x, "Hello, World!")

        """
        This is a comment - Multiline
        written in
        more than just one line
        """
        print("Hello, World!")

        #Variables are containers for storing data values.
        #A variable is created the moment you first assign a value to it.
        x = 4       # x is of type int
        x = "Sally" # x is now of type str
        print(x)

        #Casting -to specify the data type of a variable, this can be done with casting.
        x = str(3)    # x will be '3'
        y = int(3)    # y will be 3
        z = float(3)  # z will be 3.0
        print("Casting:", x,y,z)

        #GetType
        x = 5
        y = "John"
        print(type(x))
        print(type(y))

        #Case sensitive - variables
        a = 4
        A = "Sally"
        print("case:", a,A)
        #A will not overwrite a

        """
        A variable name must start with a letter or the underscore character
        A variable name cannot start with a number
        A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        Variable names are case-sensitive (age, Age and AGE are three different variables)
        A variable name cannot be any of the Python keywords.
        """
        myvar = "John"
        my_var = "John"
        _my_var = "John"
        myVar = "John"
        MYVAR = "John"
        myvar2 = "John"

        #my-var ="as" #illegal

        """
        Camel Case
        Each word, except the first, starts with a capital letter:
        """
        myVariableName = "John"

        """
        Pascal Case
        Each word starts with a capital letter:
        """
        MyVariableName = "John"

        """
        Snake Case
        Each word is separated by an underscore character:
        """
        my_variable_name = "John"

        #multiple values assignment
        x, y, z = "Orange", "Banana", "Cherry"
        print(x)
        print(y)
        print(z)

        #one value assign to multiple variables
        x = y = z = "Orange"
        print(x)
        print(y)
        print(z) 

        #unpacking - If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
        #unpack a list
        fruits = ["apple", "banana", "cherry"]
        x, y, z = fruits
        print(x)
        print(y)
        print(z)

        x = "Python "
        y = "is "
        z = "awesome"
        print("str concat:", x + y + z)


        x = 5
        y = 10
        print(x + y)

#built-in data types
"""
        Text Type:	str
        Numeric Types:	int, float, complex
        Sequence Types:	list, tuple, range
        Mapping Type:	dict
        Set Types:	set, frozenset
        Boolean Type:	bool
        Binary Types:	bytes, bytearray, memoryview
        None Type:	NoneType
"""

def func_builtinDT():
        print("\n######################## data type #############################\n")
        x ="data type"
        print(x) #str

        x = 5
        print(type(x))

        x = 20 #int
        print(x)

        x = 3.5 #float
        print(x)

        x =1j #complex
        print(x)

        x = ["apple", "banana", "cherry"] #list
        print(x)

        x = ("apple", "banana", "cherry") #tuple
        print(x)

        x = {"apple", "banana", "cherry"} #set
        print(x)

        x = frozenset({"apple", "banana", "cherry"}) #frozenset
        print(x)

        x = range(6) #range
        print(x)

        x ={"name":"om", "age":36} #dict
        print(x)

        x = True #bool
        print(x)

        x =b'Hello'
        print(x)

        x = bytearray(5) #bytearray
        print(x)

        x = memoryview(bytes(5)) #memoryview
        print(x)

        x = None #Nonetype
        print(x)

        x = 35e3
        y = 12E4
        z = -87.7e100

        print(type(x))
        print(type(y))
        print(type(z))

        #type casting
        print(str(x))
        print(int(y))
        print(float(z))

        #random
        print("Random No:", random.randrange(1, 10))

def func_string():
        x = "Hello World"
        print(x[1])

        for i in x:
                print(i)

        print("len:", len(x[1]))

        txt = "Hello free world"
        print("free" in txt)

        txt = "The best things in life are free!"
        if "free" in txt:
                print("Yes, 'free' is present")
        
        if "free1" not in txt:
                print("Yes, 'free1' is not present")

        #Slicing
        print(x[1:4])
        print(x[:5], x[2:])#Hello

        print(x.upper())
        print(x.lower())
        print(x.strip())
        print(x.replace('H', 'h'))
        print(x.split())
        print(x.splitlines())

        a ="Hello"
        b ="World"
        print(a+b)

        y = 81
        print(a+b, y)

        '''F-Strings
        F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
        To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.'''
        txt = f"Hello world, year {y}"
        print(txt)

        #display price with 2 decimals and perform calc
        txt = f"The price is {y:.2f} dollars for {20*81} items"
        print(txt)

        print("We are the so-called \"Vikings\" from the north.") #escape sequence
        print(txt.find("price")) #find the string start location
        print(txt.find("e", 5, 10))
        #print(txt.index("viking")) #raise exception

# Fibonacci series:
# the sum of two elements defines the next
def fib(num):
        a, b = 0, 1
        while a < num:
                #use eyword argument end can be used to avoid the newline after the output, or end the output with a different string:
                print(a, end=' ')
                a, b = b, a+b

#control flow statement
def if_check():
        x = int(input("\nPlease enter an integer: "))
        #Please enter an integer: 42
        if x < 0:
                x = 0
                print('Negative changed to zero')
        elif x == 0:
                print('Zero')
        elif x == 1:
                print('Single')
        else:
                print('More')

#loop control
def for_loop():
        vehicle = ['car', 'auto', 'plane', 'bike']
        for v in vehicle:
                print(v, len(v))

###################################################################
################JSON loads
###################################################################
#JSON Test - JSON to python
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#JSON Test - python to JSON
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

##################################################################
################iterate copy
##################################################################
def for_copy_userd():
# Create a sample collection
        users = {'Anbu': 'active', 'Mani': 'inactive', 'Kirsn': 'active'}

        # Strategy:  Iterate over a copy
        for user, status in users.copy().items():
                if (status == 'inactive'):
                        print("Deleting user::", user)
                        del users[user]

        # Strategy:  Create a new collection
        active_users = {}
        for user, status in users.items():
                if (status == 'active'):
                        print("Active user::", user)
                        active_users[user] = status

##################################################################
################Range check 
##################################################################
a1 = list(range(1,11))
a2 = list(range(1,20, 2))
a3 = list(range(1,30, 3))
a4 = list(range(-1,-10, -3))
print(a4)

def for_range_check():
        for i in range(10):
                print("Range::",i)
                print(a1[i], a2[i], a3[i])
        print(a2)
        print(a3)

        #string range len
        a = ['Mary', 'had', 'a', 'little', 'lamb']
        for i in range(len(a)):
                print(i, a[i])

        #finding sum
        s = sum(range(10))
        print(s)

        #break and continue
        for n in range(2, 10):
                for x in range(2, n):
                        if (n % x == 0):
                                print(f"{n} equals {x} * {n//x}")
                                break

                if ((n % 2) == 0):
                        print(f"Found an even number {n}")
                        continue
                print(f"Found an odd number {n}")

def prime_no_check(n):
        for i in range(2, n):
                for j in range(2, i):
                        if(i % j ==0):
                                print(i, 'equals', j, '*', i//j)
                                break
                else:
                        print(i, 'is a prime number')

def http_error(status):
    match status:
        case 400:
                return "Bad request"
        case 401 | 403 | 404:
                return "Not allowed"
        case 404:
                return "Not found"
        case 418:
                return "I'm a teapot"
        case _:
                return "Something's wrong with the internet"
#classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
                print("Origin")
        case Point(x=0, y=y):
                print(f"Y={y}")
        case Point(x=x, y=0):
                print(f"X={x}")
        case Point():
                print("Somewhere else")
        case _:
                print("Not a point")

###################################################################
#################read csv data
###################################################################
def Read_excel_data1(fname):
# Load the Excel file
        file_path = fname #"C:\\Users\\saijo\\OneDrive\\Desktop\\Learnings\\SaiSamridh\\html\\outsrc.xlsx" # Replace with the actual file path0"
        
        #file_path = "outsrc.csv" # Replace with the actual file path0"
        
        sheet_name = 'Sheet1'  # Replace with the actual sheet name if needed
        data = pd.read_csv(file_path)
        print(data)

        print(data.columns.ravel()) #display column list headers

        print(data['Severity'].tolist()) #get column data and convert to list

        # Extract specific field data
        # Replace 'ColumnName' with the actual column name you want to extract
        #specific_data = data['Severity']
        if ('Critical' in data['Severity']):
                specific_data = data

        #print(specific_data, data)

        # Print the extracted data
        #print(specific_data)
        #specific_data = specific_data.contain('Critical')
        #Optionally, you can save the extracted data to another file
        #if (data['Severity'].contain("Critical")):
        output_file = 'extracted_data.csv'
        specific_data.to_csv(output_file, index=False)
        print(f"Data has been saved to {output_file}")
        #exit(-2)

#read excel with specific sheet and column namres
def Read_excel_data(fname):
# Load the Excel file
        file_path = fname #"C:\\Users\\saijo\\OneDrive\\Desktop\\Learnings\\SaiSamridh\\html\\outsrc.xlsx" # Replace with the actual file path0"
        
        #file_path = "outsrc.csv" # Replace with the actual file path0"
        
        sheet_name = 'Sheet1'  # Replace with the actual sheet name if needed
        #data = pd.read_csv(file_path, sheet_name='Sheet1', usecols=['Id', 'Status', 'Severity', 'State'], header='1')
        data = pd.read_csv(file_path, usecols=['Id', 'Status', 'Severity', 'State'], encoding='utf=8')
        print(data)

        print(data.columns.ravel()) #display column list headers
        l = data['Severity'].tolist()
        print(data['Severity'].tolist()) #get column data and convert to list

        # Extract specific field data
        # Replace 'ColumnName' with the actual column name you want to extract
        specific_data = data['Severity']
        if ('Critical' in data['Severity']):
                specific_data = data

        # Print the extracted data
        print(specific_data)
        #specific_data = specific_data.contain('Critical')
        #Optionally, you can save the extracted data to another file
        #if (data['Severity'].contain("Critical")):
        j=0
        output_file = 'extracted_data.csv'
        #fp = open(output_file,'w')

        for i in l:
                if ('Critical' == i):
                        print(i)
                        print(data.iloc[j])
                        #output_file.write(data)
                        df1 = data._append
                        j=j+1
        
        specific_data.to_csv(output_file, index=False)
        data.to_csv(output_file, index=False)
        print(f"Data has been saved to {output_file}")


#############################################################################
#function invoke
#############################################################################
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Two Input Boxes")

# Create labels and input boxes
label1 = tk.Label(root, text="Input Box 1:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Input Box 2:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create a button to display the input values
def display_inputs():
    value1 = entry1.get()
    value2 = entry2.get()
    print(f"Input 1: {value1}")
    print(f"Input 2: {value2}")

button = tk.Button(root, text="Submit", command=display_inputs)
button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
        
n = 10; #Enter Fib series
fib(n)

if_check()
for_loop()
for_copy_userd()
for_range_check()
prime_no_check(n)

var=n
where_is(Point(1, y=var))
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
exit()

myfunc()
#print("Python is " + x) #error
print("Python is " + x1)

fname = sys.argv[1]
Read_excel_data(fname)
print(fname, "****\n")
func_var()
func_builtinDT()
func_string()
