def acircle(r):
    a = 3.14*r*2;
    return a

def f_to_c(t):
    n = 5*(t-32)/9
    return n

def c_to_f(t):
    n = ((t*9)/5)+32
    return n

def area(type_, s):
    if type_ == "circle":
        print("Area  of circle:", acircle(s))
    elif type_ == "square":
        print("Area of square:", s*s)
    else:
        print("Not sure")

def absv(n):
    if n >=0:
        n1 = n
    else: 
        n1 = -n
    print("absv of %d is %d", n, n1)
    
if __name__ == "__main__":
    r =float(input("Enter radius:"))
    ar = acircle(r)    
    print("Area of circle:", acircle(r), ar)

    area("circle", 3)
    area("square", 4)
    area("rect", 5)
    absv(0)
    absv(-2)

    t =float(input("Enter Fahrenheit:"))
    t = f_to_c(t)    
    print("Celcius"":", t)

    t =float(input("Enter Celcius:"))
    t = c_to_f(t)    
    print("Fahrenheit"":", t)

    name ="J'obrien"
    name1 ='J"obrien'
    print(name, name1)

# - Exercises2.py *- coding: utf-8 -*-
"""
Python has lists. The empty list is []. The following is a list of one
item ["a"] and so is [3]. Here is a list with 3 items ["ball",3.14,-2]. Let's
define a list, I'll call it lis and we'll do things with it to illustrate
accessing items in a list. Execute the following cell with Ctrl-Enter.
"""
#%%
lis = ["a","b","c","d","e","f"]
#%%
def list_exercises():
    print("The first item in the list is", lis[0])
    print("The second item in the list is", lis[1])
    print("The length of the list is", len(lis))
    print("The last item in the list is", lis[-1])
    print("Items 2 and 3 are", lis[2:4])
    print("Items up to 4 are", lis[:4])
    print("Items starting with 3 are", lis[3:])
    lis.append("g")
    print("After appending 'g' to the list, it is now", lis)
    print("'a' in lis?", "a" in lis)
    print("'r' in lis?", "r" in lis)

    for i in range(0, len(lis)):
        print(lis[i])

""" 
Exercise:
Some of the things that we can do with lists. Let's try them together.

lis[0] is the first element of the list. (index is 0)
lis[1] is the second element of the list and so on. (index is 1)
The length of the list is len(lis) and is the number of items in the list.
lis[-1] is the last item in the list.
lis[2:4] will list items 2 and 3 (but not 4)
lis[:4] will list items 0, 1, 2, 3 (but not 4); that is all items up to 4
lis[3:] will list all items starting with item 3.
lis.append("g") will append "g" onto the end of the list
"a" in lis          # running this statement will return True
"r" in lis          # running this statement will return False

Everything in Python is an object, whether it is a variable like x or a list
like lis. Objects have methods indicated by the dot. So .append() is a method
of the list object. We'll see more of this.
"""
"""
Here is an example function using a list. We pass in a list of items and
it checks for certain animals or flowers in the list.
We'll try it out on several lists such as ['bear'], ['daisy', lion'], etc.
"""
#%%

def who_is_there(lis):
    if "bear" in lis:
        print("There's a bear.")
    if "lion" in lis:
        print("There's a lion.")
    if "daisy" in lis or "iris" in lis:
        print("There are flowers.")
    if "daisy" in lis and "iris" in lis:
        print("There are at least two flowers.")
    if "donkey" in lis:
        print("There is a donkey.")
    if "horse" not in lis:
        print("There is no horse in the list.")
    print("The list has",len(lis), "items")  
#%%
"""
You should make up some lists and pass to 'who_is_there' to see how the if
statements handle various combinations. Some test lists for who_is_there:
"""

#%%
alion = ['lion']   
ld = ['lion','daisy']
lbf = ['lion','bear','iris']
str_lis = ["bear","lion","daisy","donkey","horse","iris"]

who_is_there(alion)
who_is_there(ld)
who_is_there(lbf)   
who_is_there(str_lis)

#%%
"""
The following function illustrates using lists in 'for' loops. Note that the
loop variable 'let' steps through the list, alist, taking the value of each of
its items in turn.
"""
#%%
lis = ["a","b","c","d","e","f"]
lis1 = ["a","b","a","r","c","a","a"]
#%%
def count_a(alist):
    ct = 0
    for let in alist:
        if let == 'a':
            ct = ct + 1
    print("There are",ct,"letter a's in the list.")
#%%
"""
Note there is a basic design pattern to these lists. Some variable for 
accumulating the results (above it is ct) is initiated before entering the
loop. This variable is updated within the loop. Afterwards that variable is
used (in this case ct is printed out).    
"""
count_a(lis)
count_a(lis1)
#%%

"""
Exercise:
Take the following list, nlis, and compute its average. That is, write
a function 'average(numlis)' that uses a 'for' loop to sum up the numbers
in numlis and divide by the length of numlis. Just to be sure that you
got all the numbers in numlis, print each one in your 'for' loop and 
print the length of the the list. When using a loop, one always needs to
be careful that it loops as often as is expected. In this case also print out
the number of items in the list.
Caution: Do NOT use the variable nlis in your function. This function should
work on any list of numbers. Just to be sure make sure that your function
(without any changes) works on rlis as well as nlis. 
"""
#%%
nlis = [2,4,8,105,210,-3,47,8,33,1]  # average should by 41.5
rlis = [3.14, 7.26, -4.76, 0, 8.24, 9.1, -100.7, 4] # average is -9.215
#%%
# some tests for your function. Be sure your function works for these
#%%
"""
Solution:
"""
#%%
def average(numlis):
    total = 0
    for num in numlis:
        print(num)
        total += num
    print("The average is", total / len(numlis))
#%%
average(nlis)
average(rlis)

"""
End solution
"""
""" 
Let me emphasize that you can make a 'for' loop with just a list. 
One can simply step through a list to form the loop.

In this example case it is a list of states and we will simply be stepping 
through the loop and printing out the states.
"""
#%%
newEngland = ["Maine","New Hampshire","Vermont", "Rhodes Island", 
"Massachusetts","Connecticut"]

def for_state(slis):
    for state in slis:
        print(state)
        
#%%
"""
Keep in mind that a 'for' loop can step through various kinds of iterators.
"""
for_state(newEngland)
for_state(["New York", "New Jersey", "Pennsylvania"])
for_state(range(1,10,2))  # steps through the odd numbers from 1 to 9   

"""
Exercise:
Write a function 'print_list(lis)' that prints items of the list lis. Test it 
by running the three tests that I give here. This requires writing a function 
that includes a loop like the one above, but uses lis for the iterator. Inside
your function you should use lis to represent the list. If you do so, your
function should pass all three tests below.
"""
#%% 
letter_list = ['a', 'b', 'c']
cap_list = ['A', 'B', 'C', 'D']
misc_list = ['ball', 3.14, -50, 'university', "course"]
#%%
"""
Solution:
"""
#%%
def print_list(lis):
    for item in lis:
        print(item)

print_list(letter_list)
print_list(cap_list)
print_list(misc_list)
#%%
"""
End solution
"""

"""
Lets' talk about data types. For starters Python has integers (e.g., 40), float
or real numbers (e.g., 40.0), string ("hello"), list ( ['a','b','c']), bool
(boolean -- that is, True or False). In Python they are called int, float, 
str, list, bool. You can tell what type a variable x is by entering type(x). 
Here is an example of several:
"""
#%%
x = 17      # integer
y = 3.14    # float
z = "The Walrus and the Carpenter"  # string
z1 = "30"   # string
z2 = '40'   # string
vowels = ['a','e','i','o','u'] # list of strings
nums = ['1','2','3', '3.14'] # list of strings
phrases = ["â€™Twas brillig, and the slithy toves", 
    "Did gyre and gimble in the wabe:"] # list of strings (2 strings, in fact)
r = True    # boolean
s = False   # boolean
#%%
"""
Often you can convert one type to another: int(z1) makes and returns an 
integer (30); float(z2) returns a float or real number (40.0); str(y) returns 
the string "3.14"; etc.
This is important because z1+z2 is not 70 (it is '3040'); however, 
int(z1)+int(z2) is 70. Here is a simple program showing when you might want to 
use this technique.
"""
#%%
def multiply():
    numstr1 = input("Enter a number: ")
    numstr2 = input("Enter another number: ")
    num1 = float(numstr1)
    num2 = float(numstr2)
    print("Their product is ", num1 * num2)
#    print("Won't work: ", numstr1 * numstr2)
#%%
if __name__ == "__main__":
    multiply()

"""
Compare list(range(2,20,3)) and range(2,20,3). The first one is a list and
the second one is what Python calls an iterator. The second one dishes out
the next element in the list each time it is called. This is one of the changes
from Python 2 to Python 3. In Python 2 it was a list and there was a function
xrange() for iterating without building the list. That is gone from Python 3.
Can you think of a reason that using range in Python 2 might not be a good idea
with huge lists?
""" 
#%%   
print(list(range(2,20,3)))
print(range(2,20,3))
#%%
"""
Caution: Notice that large numbers never include commas. Compare these two
examples. In the second, Python thinks that it is printing 3 numbers not 1.
"""
print(12345678)
print(12,345,678)  
#%% 
"""
Another caution. The following are Python keywords. They have special meaning
and shouldn't be used as variable names:
and         del     from    not     while
as          elif    global  or      with
assert      else    if      pass    yield
break       except  import  print
class       exec    in      raise
continue    finally is      return
def         for     lambda  try

You'll just get a syntax error:
""" 
#%%
#except = 5
#%%
"""
Note: for readability, if you feel that you need to use one of these as a 
variable, you could use an underscore after it. For example, and_, class_, etc.
That makes it different from the Python keyword.
"""
#%%
newEngland = ["Maine","New Hampshire","Vermont", "Rhodes Island", 
"Massachusetts","Connecticut"]

def for_state(state_list):
    for state in state_list:
        print(state)
        
#%%
"""
Let's print a small report. Here is a list of New England states and
their populations. We'll print this as a table or report. Essentially, this 
is like the little function above, except that we need to handle the variables 
in a more sophisticated way.
"""
#%%
newEngland = [["Massachusetts",6692824],["Connecticut",3596080],
              ["Maine",1328302],["New Hampshire",1323459],
              ["Rhode Island",1051511],["Vermont",626630]]
#%% 
"""
Exercise:
Before writing the function, let's understand this list of lists better.
Try this out. 
What is the first item of newEngland? (i.e., the one of index 0)
What is the second item?
What is the name of the state in the second element? How do we get that?
What is the population of the state in the second element?
"""
"""
Solution:
"""
def report(state_data):
    print("Population          State")
    for state_item in state_data:
        print(state_item[1], "        ", state_item[0])
        
        #What is the first item of newEngland? (i.e., the one of index 0)
        print(state_item[1], "        ", state_item[0])

        #What is the second item?
        print(state_item[1], "        ", state_item[0])
        #What is the name of the state in the second element? How do we get that
        print(state_item[1], "        ", state_item[0][1])
        #What is the population of the state in the second element?
        print(state_item[1], "        ", state_item[0][0])
#%%
report(newEngland)

#%%
"""
End solution
"""
#%%
newEngland = [["Massachusetts",6692824],["Connecticut",3596080],
              ["Maine",1328302],["New Hampshire",1323459],
              ["Rhode Island",1051511],["Vermont",626630]]
              
def report1(state_data):
    """ prints population report """
    print("Population          State")
    for state_item in state_data:
        print(state_item[1], "        ", state_item[0])

#%% 
""" 
Note: that because we pass the list into the function by way of the argument 
state_data, the above works on the following mid-Atlantic list. Execute the
following cell to define midAtlantic in IPython and try it:
"""
#%%
midAtlantic = [["New York",19746227],["New Jersey",8938175],
               ["Pennsylvania",12787209]]  
#%%
"""
Note that we don't use 19,746,227 as the population of New York. Why?
"""
""" 
Another way to do it.
"""
#%%
newEngland = [["Massachusetts",6692824],["Connecticut",3596080],
              ["Maine",1328302],["New Hampshire",1323459],
              ["Rhode Island",1051511],["Vermont",626630]]
              
def report2(state_data):
    """ prints population report """
    print("Population          State")
    for i in range(0,len(state_data)):
        print(state_data[i][1], "        ", state_data[i][0])

#%%

""" 
Find the sum of the populations of the New England states. Print
out how many there are. Use a basic loop design pattern.
"""
#%%
newEngland = [["Massachusetts",6692824],["Connecticut",3596080],
              ["Maine",1328302],["New Hampshire",1323459],
              ["Rhode Island",1051511],["Vermont",626630]]
              
def population(state_data):
    """ Sums state populations """
    sum_ = 0
    num_states = len(state_data)
    for i in range(0,num_states):
        one_state = state_data[i]
        pop = one_state[1]
        sum_ = sum_ + pop
    print("The total population of this list of states is",sum_)
    print("There are",num_states,"states in this list of states.")
#%%
    
""" 
Version using more syntactic sugar -- the variables have better and more 
meaningful names. This may read better in a bigger program. 
"""
#%%
def population(state_data):
    """ Sums state populations """
    population = 1
    sum_ = 0
    num_states  = len(state_data)
    for state in range(0,num_states):
        sum_ = sum_ + state_data[state][population]
    print("The total population of this list of states is",sum_)
    print("There are",num_states,"states in this list of states.")
#%%

"""
Exercise:
Write a function 'average(nlis)' that uses a 'for' loop and 'range()' to sum up 
the numbers in nlis and divide by the length of nlis. Just to be sure that you 
have used all the numbers in nlis, print each one in your 'for' loop and print 
the length of the list. Do not use the variable numlis in your function! If you 
change to a different list will it work? For numlis, the output should look 
like:

65 44 3 56 48 74 7 97 95 42 
the average is 53.1
"""
#%%
numlis = [65, 44, 3, 56, 48, 74, 7, 97, 95, 42]  # test on this list
numlis2 = [4,6,8,12,2,7,19]     # test on a second list to be sure
#%%
"""
Solution Starter:
"""
#%%
#def average(nlis):
#    pass  # delete this and enter your code starting here
average(numlis)
average(numlis2)

#%%    
#%%
"""
End solution
"""
"""
Libraries. Python is a "small" language in the sense that many tools 
that are available are not automatically included when you run it. Many of 
these tools are in modules called libaries and can be loaded into your program
only when you need them, keeping your programs smaller when they aren't needed. 
A typical way of doing that is 

import random

which will load the library named random.
"""
#%%
import random
#%%
# Each run of the following gives a different random number between 0 and 1
print(random.random())  
#%%
# Each run of the following gives a different random integer between 3 and 8
print(random.randint(3,8))
#%%
"""
The following example builds a sentence using various parts of speech.
It randomly chooses words from a list by using random.choice(), a function
or method imported from a library called random. We have used a method of the
string data type to capitalize the first letter of the sentence.
"""
#%%
import random

verbs=["goes","cooks","shoots","faints","chews","screams"]
nouns=["bear","lion","mother","baby","sister","car","bicycle","book"]
adverbs=["handily","sweetly","sourly","gingerly","forcefully","meekly"]
articles=["a","the","that","this"]

def sentence():
    article = random.choice(articles)    
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    
    our_sentence = article + " " + noun + " " + verb + " " + adverb + "."
    our_sentence = our_sentence.capitalize()
    
    print(our_sentence)  
#%%   

"""
Exercise:
Adapt this function to write a four line poem. Call it simple_poem().
Essentially you have to write a loop around this so that you get 4 lines.
Remember that the inside or scope of the loop has to be indented 4 spaces.
Note: The Edit menu has a quick way to indent a series of lines. The function
is repeated here for your convenience in modifying it.
"""
"""
Solution (modify the copy below to be your simple_poem function):
"""

#%%
import random

verbs=["are","is","goes","cooks","shoots","faints","chews","screams"]
nouns=["bear","lion","mother","baby","sister","car","bicycle","book"]
adverbs=["handily","sweetly","sourly","gingerly","forcefully","meekly"]
articles=["a","the","that","this"]

def simple_poem():
    article = random.choice(articles)    
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    
    our_sentence = article + " " + noun + " " + verb + " " + adverb + "."
    our_sentence = our_sentence.capitalize()
    
    print(our_sentence)
    print(our_sentence)
    print(our_sentence)
    print(our_sentence)

simple_poem()   
#%%
"""
End Solution:
"""
"""
Let's look at a couple of loop design patterns.
"""
"""
Example: Add numbers until you get a blank one. This initializes a variable
sum_ and adds to it each time through the loop. Afterwards sum_ is used in a
print statement.
"""
#%%
def add_up():
    sum_ = 0
    while True:             # will loop forever
        num = int(input("Enter a number, input 0 to quit: "))
        if num == 0:
            break           # breaks out of while loop
        sum_ = sum_ + num
    print(sum_)
#%%
if __name__ == "__main__":
    add_up()

""" 
Building lists - recall the .append() method 
"""
#%%
baseball = []
baseball.append("ball")
baseball.append("bat")
baseball.append("mitt")
baseball
#%%
""" 
Let's write a program to build a list of the numbers. Before we initialized 
sum_ to 0. The equivalent for a list is to set it to the empty list. Adding to
the sum has its equivalent in appending to the list.
"""
#%%    
def store_up():
    num_lis = []
    while True:
        nextnum = int(input("Enter a number, 0 to quit: "))
        if nextnum == 0:
            break
        num_lis.append(nextnum)
    print(num_lis)
#%%
"""
Exercise:
Write a function diner_waitress() that asks for you order. First start an empty
list, call it order. Then use a while loop and an input() statement to gather
the order. Continue in the while loop until the customer says "that's all". 
Onne way to end the loop is to use 'break' to break out of the loop when 
"that's all" is entered. 
Recall that you can add to a list by using the list's .append() method; suppose
that your list is called order. To create an empty list you can use
order = []. You are going to have to input one food at a time and append it
to the order list.
Then print out the order. Here is my run:

diner_waitress()
Hello, I'll be your waitress. What will you have?

menu item: eggs

menu item: bacon

menu item: toast

menu item: jelly

menu item: that's all
You've ordered:
['eggs', 'bacon', 'toast', 'jelly']

"""
#%%
"""
Solution:
"""
def diner_waitress():
    order = []
    print("Hello, I'll be your waitress. What will you have?")
    while True:
        item = input("menu item: ")
        if item.lower() == "that's all":
            break
        order.append(item)
    print("You've ordered:")
    print(order)
#%%

diner_waitress()

#%%

#Classes. A class is a way to define a new data type. It is a template for creating objects. 
# An object is an instance of a class. A class can have attributes (data) and methods (functions that operate on the data). 
# Here is a simple example of a class for a Dog.
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog('Buddy', 'Golden Retriever')
print(my_dog.bark()) # Output: Buddy says woof

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        return f"{self.name} says meow!"

my_cat = Cat('Whiskers', 'Orange')
print(my_cat.meow()) # Output: Whiskers says meow!

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

my_circle = Circle(5)
print(my_circle.area()) # Output: 78.5  

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

my_rectangle = Rectangle(4, 6)
print(my_rectangle.area()) # Output: 24

class area:
    def __init__(self, shape, dimensions):
        self.shape = shape
        self.dimensions = dimensions

    def calculate_area(self):
        if self.shape == 'circle':
            radius = self.dimensions[0]
            return 3.14 * radius ** 2
        elif self.shape == 'rectangle':
            width, height = self.dimensions
            return width * height
        else:
            return "Shape not supported"    

my_area_circle = area('circle', [5])
print(my_area_circle.calculate_area()) # Output: 78.5
my_rectangle_area = area('rectangle', [4, 6])
print(my_rectangle_area.calculate_area()) # Output: 24

class calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

my_calculator = calculator()
print(my_calculator.add(10, 5)) # Output: 15

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

my_car = car('Toyota', 'Camry', 2020)
print(my_car.description()) # Output: 2020 Toyota Camry

#inheritance. A class can inherit from another class, which means it can use the attributes and methods of the parent class. Here is an example of a class for a Dog that inherits from an Animal class.
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."    
    def speak(self):
        pass

class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"
    def speak(self):
        return f"{self.name} says woof!"

my_dog = Dog('Buddy')
print(my_dog.eat()) # Output: Buddy is eating.
print(my_dog.bark()) # Output: Buddy says woof!

my_pet = Dog('Max')
print(my_pet.speak()) # Output: Max says woof

#polymorphism. Polymorphism is the ability of different classes to be treated as instances of the same class through inheritance. 
# For example, if we have a function that takes an Animal object and calls its speak method, it can work with any subclass of Animal, 
# such as Dog or Cat.
class Bird:
    def speak(self):
        return "Tweet!"
class Cat:
    def speak(self):
        return "Meow!"

animals = [Bird(), Cat()]
for animal in animals:
    print(animal.speak()) # Output: # Tweet! # Meow!

#encapsulation. Encapsulation is the concept of hiding the internal state and behavior of an object and only exposing a public interface. 
# This can be achieved in Python by using private attributes and methods. Private attributes are defined with a double underscore 
# prefix, and they cannot be accessed directly from outside the class.
#abstract classes and interfaces. An abstract class is a class that cannot be instantiated and is meant to be subclassed. 
# It can have abstract methods, which are methods that are declared but not implemented in the abstract class. 
# An interface is a type of abstract class that only contains abstract methods and no implementation.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

account = BankAccount(1000)
print(account.deposit(500)) # Output: 1500
#print(account.__balance) # Error: AttributeError

#Generators. A generator is a special type of iterator that allows you to iterate over a sequence of values without storing them all in memory at once. 
# You can create a generator using a function with the yield keyword. Example of a generator that generates the Fibonacci sequence.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b 

for num in fibonacci(10):
    print(num) # Output: 0 1 1 2 3 5 8 13 21 34

def generator_example():
    for i in range(5):
        yield i * i

for square in generator_example():
    print(square) # Output: 0 1 4 9 16

def count_up_to(n):
    count = 0
    while count < n:
        yield count
        count += 1

for number in count_up_to(5):
    print(number) # Output: 0, 1, 2, 3, 4

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)# Output: 5, 4, 3, 2, 

def comprehension_example():
    # List comprehension to create a list of squares
    squares = [x**2 for x in range(10)]
    print(squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

comprehension_example()

squares_gen = (x**2 for x in range(10)) # Generator expression
for square in squares_gen:
    print(square) # Output: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81

''' W6
1. Generators (Efficient Sequences)
Task 1: Write a generator function generate_even_numbers(n) that yields even numbers up to n.
Task 2: Create a generator expression to generate squares of numbers from 1 to 10 and print the output.
Task 3: Write a generator function to yield Fibonacci numbers up to n terms.
'''

def generate_even_numbers1(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def generate_square_numbers1(n):
    squ = [x * x for x in range(n)]
    return squ

def generate_fib_numbers1(n):
    i=0
    j=1
    c=0
    print(i, j)
    for _ in range(n):
        yield i
        c = i +j
        i = j
        j = c
        #print(c)

generate_even_numbers1(10)
generate_square_numbers1(10)
generate_fib_numbers1(10)

for num in generate_even_numbers1(10):
    print(num)

'''
for square in generate_square_numbers(10):
    print(square)

for fib in generate_fib_numbers(10):
    print(fib)
'''

''' W6
1. Generators (Efficient Sequences)
Task 1: Write a generator function generate_even_numbers(n) that yields even numbers up to n.
Task 2: Create a generator expression to generate squares of numbers from 1 to 10 and print the output.
Task 3: Write a generator function to yield Fibonacci numbers up to n terms.
'''
#Generators
def generate_even_numbers(n):
    for i in range(n):
        if (i%2==0):
            yield i
            #print(i)

for n in generate_even_numbers(10):
    print(n)
#generate_even_numbers(10)

def generate_square_numbers(n):
    squ =[x*x for x in range(n) ]
    return squ

squares_gen = (x**2 for x in range(10)) # Generator expression
for square in squares_gen:
    print(square) # Output: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81

def generate_fib_numbers(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b 
        #print(a)

for n in generate_fib_numbers(10):
    print(n)

def fib_numbers(n):
    a = 0
    b = 1
    print(a)
    for i in range(n):
        #yield a
        a, b = b, a + b 
        #print(a)

#fib_numbers(10)

'''Section 2: Iterators 
4. Create a list of strings. Obtain an iterator from the list and print each element using 
next(). 
5. Create an iterator to iterate over a dictionary and print both keys and values
'''
#Iterators
def func_iter():
    strlist = ['dog', 'cat', 'cow', 'tiger','lion','elephant']
    iobj = iter(strlist)
    print(next(iobj))
    print(next(iobj))
    print(next(iobj))

    for io in iobj:
        print(io)

func_iter()

def func_dict():
    mdict ={'Ram':35, 'Raj':36, 'Rah': 37}
    for k, v in mdict.items():
        print(k,v)

func_dict()

'''
Section 3: Decorators 
6. Write a simple decorator that prints "Function is being called" before the execution of 
the actual function. 
7. Create a decorator that logs the execution time of a function. Use the time module. 
8. Write a decorator that checks if the user is authenticated (simulate with a Boolean 
variable is_authenticated), and only then allows the function to run. If not authenticated, 
print "Access Denied". 
'''
#Decorator
def f_decorator(func):
    def fwrapper():
        print("Function is being called")
        func()
    return fwrapper

@f_decorator
def func_iter1():
    strlist = ['dog', 'cat', 'cow', 'tiger','lion','elephant']
    iobj = iter(strlist)
    print(next(iobj))
    print(next(iobj))
    print(next(iobj))

    for io in iobj:
        print(io)

func_iter1()

import time
def f_decorator_logtime(func):
    def fwrapper(*args, **kwargs):
        t1 = time.time()
        r = func(*args, **kwargs)
        t2 = time.time()
        print(f'Time:{t2-t1} seconds')
        return r
    return fwrapper

@f_decorator_logtime
def my_func():
    time.sleep(1)

my_func()

is_authenticated = False
def f_decorator_check(func):
    def fwrapper():
        if(is_authenticated == True):     
            my_funcT()
        else:
            print("Access Denied")
    return fwrapper

@f_decorator_check
def my_funcT():
    print("Secured access allowed")

my_funcT()

'''
Section 4: Context Managers 
9. Use the built-in with open() context manager to read a text file and print its contents. 
10. Write a context manager using the contextlib module that temporarily changes the 
working directory, and prints the current directory inside the context and restores it 
afterward. 
'''

text = (
    "Section 4: Context Managers "
    "Use the built-in with open() context manager to read a text file and print its contents. "
    "10. Write a context manager using the contextlib module "
    "that temporarily changes the working directory, prints the current directory inside "
    "the context, and restores it afterward."
)

f = open('sample.txt', 'w')
f.write(text)
f.close()

def openf():
    file = open('sample.txt', 'r')
    try:
        data = file.read()
        print(data)
    finally:
        file.close()  # Ensures the file is closed even if an error occurs
        
def openf_with():
    with open('sample.txt', 'r') as file:
        data = file.read()
        print(data)

openf_with()

import os
from contextlib import contextmanager

@contextmanager
def chg_dir(npath):
    ppath = os.getcwd()
    os.chdir(npath)
    try:
        yield
    finally:
        os.chdir(ppath)

with chg_dir("/tmp"):
    print("Inside context:", os.getcwd())
print("restored", os.getcwd())
#exit()

#numpy. Numpy is a powerful library for numerical computing in Python. It provides support for arrays, matrices, and a wide range of 
# mathematical functions. Here are some examples of using numpy: 
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr) # Output: [1 2 3 4 5]
print(arr**2) # Output: [ 1  4  9 16 25]
print(arr*2) # Output: [ 2  4  6  8 10]
print(arr.mean()) # Output: 3.0
print(arr.sum()) # Output: 15
print(arr[0]) # Output: 1
print(arr[1:4]) # Output: [2 3 4]
print(arr[arr > 2]) # Output: [3 4 5]
print(arr.shape) # Output: (5,)
print(arr.ndim) # Output: 1
print(arr.dtype) # Output: int64
print(arr.size) # Output: 5
print(arr.itemsize  ) # Output: 8 (bytes per element )
print(arr.reshape(5,1)) # Output: [[1] [2] [3] [4] [5]]

#pandas. Pandas is a library for data manipulation and analysis. It provides data structures like Series and DataFrame, 
# which are built on top of numpy arrays. Here are some examples of using pandas:
#!pip install pandas
import pandas as pd

print(pd.__version__) # Output: 1.3.2 (or whatever the current version is

c_age = pd.Series([23,45,67,56,67,90,82])
print(c_age) # Output: 0    23
              #         1    45
              #         2    67
              #         3    56
              #         4    67
              #         5    90
              #         6    82
print(type(c_age)) # Output: <class 'pandas.core.series.Series'>
print(c_age.mean()) # Output: 63.714285714285715
print(c_age.median()) # Output: 67.0
print(c_age.dtype) # Output: int64
age = c_age+5 # Output: 0    28
          #         1    50
            #         2    72


c_age = pd.Series([25, 30, 35], index=['Alice', 'Bob', 'Charlie'])
print(c_age) # Output: Alice      25
             #         Bob        30
             #         Charlie    35

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df) # Output:    Name  Age         City
          #        0  Alice   25     New York
          #        1    Bob   30  Los Angeles
          #        2 Charlie   35      Chicago
print(df['Name']) # Output: 0      Alice
                  #         1        Bob
                  #         2    Charlie

#implicit coercion. When you perform operations on pandas Series or DataFrames, pandas will automatically align the data based on the 
# index and perform implicit coercion if necessary. For example, if you add two Series with different indices, pandas will align them 
# based on the index and fill in missing values with NaN.
s1 = pd.Series([1, 2, '3',], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, '6'], index=['b', 'c', 'd'])
result = s1 + s2    
print(result) # Output: a    NaN
              #         b    6.0    

#explicit coercion. You can also explicitly convert data types in pandas using methods like astype(). 
# For example, to convert a Series of strings to integers:
s = pd.Series([1, 2, 3],dtype='int64')
s_int = s.astype(int)
print(s_int) # Output: 0    1
                #         1    2

sales_region_wise = pd.DataFrame({'Region': ['North', 'South', 'East', 'West'], 'Sales': [100, 150, 200, 250]})
print(sales_region_wise) # Output:   Region  Sales

sales_region_wise = ['North', 'South', 'East', 'West', 100, 150, 200, 250]
print(sales_region_wise) # Output:   Region  Sales
s = pd.Series(sales_region_wise[:4], sales_region_wise[4:])
print(s) # Output: 0    North
         #         1    South
         #         2    East
         #         3    West
         #         4    100
         #         5    150
         #         6    200
         #         7    250
print(s.mean()) # Output: 175.0 (average of the numeric values, ignoring the strings)
print(s.mean()) # Output: 175.0 (same as avg())
print(s==0)
print(s[s==0]) # Output: 0    False
print(type(s[0])) # Output: <class 'str'> (the first element is a string)
print(type(s[6])) 

#filtering a DataFrame. You can filter a DataFrame based on conditions. For example, to filter the DataFrame to include 
# only rows where Age is greater than 28:
filtered_df =df[df['Age']>28]
print(filtered_df) # Output:    Name  Age         City
                    #         1    Bob   30  Los Angeles
                    #         2 Charlie   35      Chicago
#grouping a DataFrame. You can group a DataFrame by a column and perform aggregate functions on the groups. For example, 
# to group the DataFrame by City and calculate the mean Age for each city:
grouped_df = df.groupby('City').mean()
print(grouped_df) # Output
                    #                 Age
                    # City
                    # Chicago       35.0
                    # Los Angeles   30.0
                    # New York      25.0

#matplotlib. Matplotlib is a library for creating static, animated, and interactive visualizations in Python. 
# Here are some examples of using matplotlib:
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.title('Square Numbers')
plt.xlabel('x')
plt.ylabel('y')
plt.show() # This will display the plot

#creating a bar chart
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]
plt.bar(categories, values)
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show() # This will display the bar chart

#creating subplots
fig, axs = plt.subplots(2, 2) # 2 rows, 2 columns of subplots
axs[0, 0].plot(x, y) # Top-left subplot
axs[0,1].scatter(x, y) # Top-right subplot
axs[1,0].bar(x, y) # Bottom-left subplot
axs[1,1].hist(y) # Bottom-right subplot
axs[0, 0].set_title('Line Plot')
axs.show() # This will display the subplots

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.subplot(2, 1, 1) # 2 rows, 1 column, first subplot
plt.plot(x, y1) 
plt.title('Sine Wave')
plt.subplot(2, 1, 2) # 2 rows, 1 column, second subplot
plt.plot(x, y2)
plt.title('Cosine Wave')
plt.tight_layout() # Adjust layout to prevent overlap   
plt.show() # This will display the subplots

emp_records = pd.DataFrame({'Employee': ['Alice', 'Bob', 'Charlie'], 'Department': ['HR', 'IT', 'Finance'], 'Salary': [50000, 60000, 55000]})
print(emp_records) # Output:   Employee Department  Salary

print(emp_records['Department']) # Output: 0         HR
                                #         1         IT  
                                #         2    Finance
print(emp_records[emp_records['Salary'] > 55000]) # Output:   Employee Department  Salary
                                                #         1      Bob         IT   60000
print(emp_records.groupby('Department')['Salary'].mean()) # Output: Department
                                                        # HR            50000.0
                                                        # IT            60000.0
                                                        # Finance       55000.0
print(emp_records.loc['Alice']) # Output: Employee    Alice
                                # Department       HR
                                # Salary        50000                          # Name: Alice, dtype: object     

emp_records.iloc[[0,1],:] # Output:   Employee Department  Salary
                        #         0    Alice         HR   50000
                        #         1      Bob         IT   60000
emp_records.iloc[[0,2],[0,2]] # Output:   Employee  Salary
                            #         0    Alice   50000
                            #        2  Charlie   55000
                            # Note: iloc uses integer-based indexing, while loc uses label-based indexing.
                            # In this example, iloc[[0,1],:] selects the first two rows (Alice and Bob) and all columns,
                            #  while iloc[[0,2],[0,2]] selects the first and third rows (Alice and Charlie) and the first and third columns (Employee and Salary).
                            # In contrast, loc['Alice'] selects the row with the label 'Alice' and all columns.
emp_records.iloc[:2,0,2 ] # Output:   Employee Department  Salary

#loc
emp_records.loc['Alice'] # Output: Employee    Alice
emp_records.loc[['Alice', 'Bob'],:] # Output: 50000

#csv
emp_records.to_csv('employee_records.csv', index=False) # This will save the DataFrame to a CSV file without the index
loaded_emp_records = pd.read_csv('employee_records.csv') # This will load the DataFrame from the CSV file
print(loaded_emp_records) # Output:   Employee Department  Salary
# %%
