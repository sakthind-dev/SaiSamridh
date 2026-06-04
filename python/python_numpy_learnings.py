# Numpy
import numpy as np

#numpy is a library in python used for working with arrays. It also has functions for working in the domain of linear algebra,
#fourier transform, and matrices.
distance = [10,15,25,40]

# np.array() is a function that converts a list into a numpy array. A numpy array is a grid of values, all of the same type,
# and is indexed by a tuple of non-negative integers.
distance_array = np.array(distance)
print(distance_array, type(distance_array))

time = [.3,.47,.9,1.2]
time_array = np.array(time)
print(time_array, type(time_array))

#will throw an error if we try to divide the two lists because they are not the same type.
#d = distance/time

#speed is distance divided by time. With numpy arrays, we can perform element-wise operations directly.
speed = distance_array/time_array
print(speed, type(speed))

speed_rounded = np.round(speed, 2)
print(speed_rounded)

#numpy also has a lot of built in functions that can be used to perform operations on arrays. 
# For example, we can use the mean function to calculate the mean of an array.
mean_speed = np.mean(speed) 
print(mean_speed, type(mean_speed)) 

# We can also use the std function to calculate the standard deviation of an array.
std_speed = np.std(speed)
print(std_speed,type(std_speed))

#Numpy also has a lot of functions for working with matrices. For example, we can use the dot function to calculate the dot product 
# of two matrices.
matrix_a = np.array([[1,2],[3,4]])
matrix_b = np.array([[5,6],[7,8]])
matrix_c = np.dot(matrix_a, matrix_b)
print(matrix_c, type(matrix_c))

# (1) Type of data by dtype
distance_array = np.array([10,15,25,40])
distance_array.dtype
distance_array.shape
distance_array.ndim
distance_array.size
print(distance_array, type(distance_array), distance_array.dtype, distance_array.shape, distance_array.ndim)

time_array = np.array([.3,.47,.9,1.2])
time_array.dtype
print(time_array, type(time_array), time_array.dtype, time_array.shape, time_array.ndim)

# Below are the 3 students how have gotten marks in Maths, Science and Socst
Marks_maths =   [34,45,89]
Marks_science = [48,55,98]
Marks_socst =   [67,36,60]

# We can create a 2D array (matrix) to represent the marks of the students in different subjects.
marks_array = np.array([Marks_maths, Marks_science, Marks_socst])   
print(marks_array, type(marks_array), marks_array.dtype, marks_array.shape, marks_array.ndim)

Total_marks = np.array(Marks_maths) + np.array(Marks_science) + np.array (Marks_socst)
print("Total Marks:", Total_marks)

#broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations.
# For example, if we want to add a constant value to each element of an array, we can do it directly without having to create a new array of the same shape.

Total_marks = Total_marks/3
Total_marks = np.round(Total_marks, 2)
print("Average Total Marks:", Total_marks)

print("Mean of Average Total Marks:", np.mean(Total_marks))
print("Standard Deviation of Average Total Marks:", np.std(Total_marks))
print("Minimum Average Total Marks:", np.min(Total_marks))
print("Maximum Average Total Marks:", np.max(Total_marks))
print("Sum of Average Total Marks:", np.sum(Total_marks))
print("Median of Average Total Marks:", np.median(Total_marks))
print("Variance of Average Total Marks:", np.var(Total_marks))
print("25th Percentile of Average Total Marks:", np.percentile(Total_marks, 25))
print("75th Percentile of Average Total Marks:", np.percentile(Total_marks, 75))
print("Unique Average Total Marks:", np.unique(Total_marks))
print("Sorted Average Total Marks:", np.sort(Total_marks))
print("Indices that would sort the Average Total Marks:", np.argsort(Total_marks))
print("Number of Average Total Marks:", np.size(Total_marks))
print("Shape of Average Total Marks:", np.shape(Total_marks))
print("Data Type of Average Total Marks:", Total_marks.dtype)
print("Number of Dimensions of Average Total Marks:", np.ndim(Total_marks))

constant_value = 10
new_marks_array = marks_array + constant_value
print("New Marks Array with Constant Added:")
print(new_marks_array)

np.mean([34,48,67])

# 2 D Array
# np.array([[row1],[row2],[row3]........])
emp_recs = np.array([[101,5],[102,7],[103,2],[104,15]])
print(emp_recs)
print("Type of Employee Records:", type(emp_recs))
print("Shape of Employee Records:", emp_recs.shape)
print("Data Type of Employee Records:", emp_recs.dtype)
print("Number of Dimensions of Employee Records:", emp_recs.ndim)
print("Number of Employee Records:", np.size(emp_recs))

#################### Converting Data types
# (1) Implicit conversion of Data type
# Char and Nums mix - Char will take precedence over numeric 
emp_details = np.array([["John",15,45],["Liz",10,30],["Barb",2,21],["Theresa",1,19],["Tim",19,50]])
print(emp_details)
print("Type of Employee Details:", type(emp_details))
print("Shape of Employee Details:", emp_details.shape)
print("Data Type of Employee Details:", emp_details.dtype)
print("Number of Dimensions of Employee Details:", emp_details.ndim)

emp1_details = np.array(["JohnC",25,55])
print(emp1_details)

print("Type of Employee 1 Details:", type(emp1_details))
# (2) Explicit conversion of Data type
emp1_details = np.array(["JohnC",25,55], dtype=object)
print(emp1_details)
print("Type of Employee 1 Details:", type(emp1_details))    

emp2_details = np.array([[15,45],[10,30],[2,"21"],[1,19],[19,50]])
print(emp2_details)
print("Type of Employee 2 Details:", type(emp2_details))
print("Shape of Employee 2 Details:", emp2_details.shape)
print("Data Type of Employee 2 Details:", emp2_details.dtype)
print("Number of Dimensions of Employee 2 Details:", emp2_details.ndim)

# understanding U11
emp3_details = np.array([["John",15,45],["Elizabeth Thompson",10,30],["Barb",2,21],["Theresa",1,19],["Tim",19,50]])
print(emp3_details)
print("Type of Employee 3 Details:", type(emp3_details))
print("Shape of Employee 3 Details:", emp3_details.shape)
print("Data Type of Employee 3 Details:", emp3_details.dtype)
print("Number of Dimensions of Employee 3 Details:", emp3_details.ndim)

#implicit conversion of data type - when we have a mix of data types in an array, numpy will automatically convert all the elements to a common data type that can accommodate all the values. In this case, since we have strings and integers, numpy will convert all the integers to strings to create a homogeneous array of strings.
emp4_details = np.array([[15,45],[10,30],[2,"21"],[1,19],[19,50]],dtype='int32')
print(emp4_details)
print("Type of Employee 4 Details:", type(emp4_details))
print("Shape of Employee 4 Details:", emp4_details.shape)
print("Data Type of Employee 4 Details:", emp4_details.dtype)  
print("Number of Dimensions of Employee 4 Details:", emp4_details.ndim)

emp5_details = np.array([[15,45],[10,30],[2,"21"],[1,19],[19,50]],dtype='int32')
emp5_details = emp5_details.astype('int32')
print(emp5_details)
print("Type of Employee 5 Details:", type(emp5_details))
print("Shape of Employee 5 Details:", emp5_details.shape)
print("Data Type of Employee 5 Details:", emp5_details.dtype)
print("Number of Dimensions of Employee 5 Details:", emp5_details.ndim)

# Can below be convered into integer datatype? - NO
emp_details = np.array([["John",15,45],["Liz",10,30],["Barb",2,21],["Theresa",1,19],["Tim",19,50]])

#invalid literal for int() with base 10: 'John' - because of the presence of string values in the array, 
# it cannot be converted to integer data type. The presence of non-numeric values prevents the conversion to integers, as they cannot be interpreted as numbers.
# emp_details = emp_details.astype('int32')
# emp_details = emp_details.astype('int64')

print(emp_details)

#Indexing array 1D, 2D
cust_age = np.array([34,23,21,45,23,25])
print(cust_age[0]) # first element
print(cust_age[3]) # fourth element
print(cust_age[1:4]) # slicing from index 1 to index 3 (4 is exclusive)
print(cust_age[:3]) # slicing from the beginning to index 2 (3 is exclusive)
print(cust_age[3:]) # slicing from index 3 to the end
print(cust_age[-1]) # last element
print(cust_age[1:]) # slicing from index 1 to the end
print(cust_age[:-1]) # slicing from the beginning to the second last element
print(cust_age[[1,5]]) # indexing with a list of indices - this will return the elements at index 1 and index 5
print(cust_age[cust_age > 25]) # boolean indexing - this will return the elements that are greater than 25
print(np.where(cust_age > 25)) # this will return the indices of the elements that are greater than 25
print(np.where(cust_age > 25, "Older than 25", "25 or younger")) # this will return an array with the same shape as cust_age, where each element is "Older than 25" if the corresponding element in cust_age is greater than 25, and "25 or younger" otherwise 
print(np.sort(cust_age)) # this will return a sorted array of cust_age

#2D Array Indexing
marks_array = np.array([[34,45,89],[48,55,98],[67,36,60]])
print(marks_array)
print(marks_array[0]) # first row
print(marks_array[1]) # second row
print(marks_array[0][1]) # element at first row and second column
print(marks_array[1][2]) # element at second row and third column
print(marks_array[0,1]) # element at first row and second column
print(marks_array[1,2]) # element at second row and third column
print(marks_array[:,0]) # all rows and first column
print(marks_array[:,1]) # all rows and second column
print(marks_array[:,2]) # all rows and third column
print(marks_array[0,:]) # first row and all columns
print(marks_array[1,:]) # second row and all columns
print(marks_array[2,:]) # third row and all columns
print(marks_array[marks_array > 50]) # boolean indexing - this will return the elements that are greater than 50
print(np.where(marks_array > 50)) # this will return the indices of the elements that are greater than 50
print(np.where(marks_array > 50, "Greater than 50", "50 or less")) # this will return an array with the same shape as marks_array, where each element is "Greater than 50" if the corresponding element in marks_array is greater than 50, and "50 or less" otherwise
print(np.sort(marks_array, axis=0)) # this will return a sorted array of marks_array along the columns
print(np.sort(marks_array, axis=1)) # this will return a sorted array of marks_array along the rows

emp_recs = np.array([[101,110,32],[102,120,34],[103,98,37],[104,99,67]])
print(emp_recs[:,1]) # all rows and second column - this will return the second column of emp_recs, which contains the salaries of the employees

#array 2D(r,c)
print(emp_recs[0:2,:]) # first two rows and all columns - this will return the first two rows of emp_recs
print(emp_recs[:,0:2]) # all rows and first two columns - this will return the first two columns of emp_recs, which contain the employee IDs and salaries
print(emp_recs[1:3,0:2]) # second and third rows and first two columns - this will return the second and third rows of emp_recs, and the first two columns, which contain the employee IDs and salaries of the second and third employees
emp_recs[[0,2],:]
emp_recs[:,0:2]
emp_recs[0:2,[0,2]]

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

matrix = np.array([[1,2],[3,4]])
print(matrix)
print(matrix.shape) # Output: (2, 2)
print(matrix.ndim) # Output: 2
print(matrix.dtype) # Output: int64
print(matrix.size) # Output: 4
print(matrix.itemsize) # Output: 8 (bytes per element)
print(np.linalg.inv(matrix)) # Output: [[-2.  1.] [ 1.5 -0.5]] (inverse of the matrix)
print(np.mean(matrix)) # Output: 2.5 (mean of all elements in the matrix)
