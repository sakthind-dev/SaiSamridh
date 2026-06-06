############W6######################
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('sales_data.csv')

# **Exercise 1: Loading Data**
# 1. Get a summary of the DataFrame
print(df.info())
# 2. Get a summary of the numeric columns
print(df.describe())

# **Exercise 2: Accessing Data**
# 1. Access the first 5 rows
print(df.head())
# 2. Access a specific column (Product or Price)
print(df['Product'].unique())  # or df['Price'].unique()
# 3. Access rows where Sales > 500
print(df[df['Sales'] > 500])

# **Exercise 3: Filtering Data**
# 1. Filter data for Region = East
print(df[df['Region'] == 'East'])
# 2. Filter data where Price > 100 and Sales < 1000
print(df[(df['Price'] > 100) & (df['Sales'] < 1000)])

# **Exercise 4: Handling Missing Values**
# 1. Check for missing values
print(df.isnull().sum())
# 2. Fill missing values in the Sales column with the median
df['Sales'].fillna(df['Sales'].median(), inplace=True)
# 3. Drop rows where Product is missing
df.dropna(subset=['Product'], inplace=True)

# **Exercise 5: Adding New Column**
# 1. Add a new column Discounted_Price (10% off)
df['Discounted_Price'] = df['Price'] * 0.9
# 2. Display the first 5 rows to confirm
print(df.head())

# **Exercise 6: Dropping Columns**
# 1. Drop the Discounted_Price column
df.drop(columns=['Discounted_Price'], inplace=True)
# 2. Confirm the column has been dropped
print(df.columns)

# **Exercise 7: Combining NumPy Functions**
# 1. Create a new column Profit (Sales - Cost)
df['Profit'] = df['Sales'] - df['Cost']
# 2. Create a new column Log_Profit using np.log()
df['Log_Profit'] = np.log(df['Profit'])
# Display the first 5 rows to confirm
print(df.head())

'''Seaborn Exercise: Visualizing Data'''
import seaborn as sns
import pandas as pd
from matplotlib import style
style.use('ggplot')
# Load Titanic dataset
titanic = sns.load_dataset("titanic")

# Display first few rows
print(titanic.head())
# dropping rows based on Age column
titanic.dropna(subset=['age'],inplace=True)

#univariate analysis
import matplotlib.pyplot as plt

# Histogram for age distribution
sns.histplot(data=titanic, x="age")
plt.title("Age Distribution")
plt.show()

# Count plot for gender
sns.countplot(data=titanic, x="sex")
plt.title("Count of Passengers by Gender")
plt.show()

#multivariate analysis
# Heatmap: Correlation between numerical variables
corr = titanic.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Pair plot for selected variables
sns.pairplot(titanic, vars=["age", "fare", "survived"], hue="class")
plt.show()

'''Faceted Visualization'''
# Faceted grid: Survival by age and sex
g = sns.FacetGrid(titanic, row="sex", col="class", hue="survived", margin_titles=True)
g.map(sns.scatterplot, "age", "fare", alpha=0.7)
g.add_legend()
plt.show()

'''Advanced Relational Plot '''
# advanced Relational plot with line segments for fare by age
sns.relplot(
    data=titanic, x="age", y="fare", kind="line",
    hue="class", style="sex", markers=True, dashes=False
)
plt.title("Fare by Age for Different Classes")
plt.show()

'''combining panels'''
# FacetGrid with segments for survival and fare
g = sns.FacetGrid(titanic, col="sex", row="class", hue="survived", height=4, aspect=1.5)
g.map(sns.lineplot, "age", "fare", alpha=0.7)
g.add_legend()
plt.show()

'''advanced Categorical Plot'''
# advanced categorical plot with boxplot and swarmplot for fare by class
import warnings
warnings.filterwarnings('ignore')
# Strip plot with jitter
plt.figure(figsize=(14,6))
sns.stripplot(data=titanic, x="class", y="age", jitter=True, hue="sex", dodge=True)
plt.title("Age Distribution by Class and Gender")
plt.show()

# Swarm plot
plt.figure(figsize=(14,6))
sns.swarmplot(data=titanic, x="class", y="fare", hue="sex", dodge=True)
plt.title("Fare Distribution by Class and Gender")
plt.show()












####################################
# Python Assignment - Control Structures, File Handling, and Comprehensions
#WK5
####################################
'''
Task 1: Control Structures - Grading System
Write a program that:
1. Takes a student's score (out of 100) as input.
2. Uses if-elif-else to assign a grade:
o 90-100: Grade A
o 80-89: Grade B
o 70-79: Grade C
o 60-69: Grade D
o Below 60: Grade F
3. Also implement a basic match-case (switch-case) to print:
o "Excellent" for Grade A
o "Good" for Grade B or C
o "Needs Improvement" for Grade D or F
'''

#Uses if-elif-else to assign a grade:
score = int(input("Enter Student score"))

if score >= 90:
    print("Grade A")
    grade = 'A'
elif score >= 80:
    print("Grade B")
    grade = 'B'
elif score >= 70:
    print("Grade C")
    grade = 'C'
elif score >= 60:
    print("Grade D")
    grade = 'D'
else:
    print("Grade F")
    grade = 'F'

#Also implement a basic match-case (switch-case) to print:

match grade:
    case 'A':
        print("Excellent")
    case 'B' | 'C':
        print("Good")
    case 'D'| 'F':
        print("Needs Improvement")
    case _:
        print("Invalid Grade")

'''
Task 2: File Handling - Student Data
Write a program that:
1. Takes 3 student names and scores as input from the user.
2. Saves the data to a file called students.txt in the format:
Name - Score
3. Then read back the file and print each line prefixed with the line number.
'''
f = open("students.txt", 'w')
num = 3

for i in range(num):
    name = (input("Enter Student name:"))
    score = (int)(input("Enter Student score"))

    f.write(f"{name}-{score}\n")

f.close()

'''
Task 3: List and Dictionary Comprehensions - Data Transformation
Using the data below:
students = [
 {"name": "Alice", "score": 85},
 {"name": "Bob", "score": 72},
 {"name": "Charlie", "score": 91},
 {"name": "David", "score": 65},
]
1. Use a list comprehension to create a list of names of students who scored above 80.
2. Use a dictionary comprehension to create a dictionary where:
o Keys are student names
o Values are "Pass" if score >= 70, otherwise "Fail"
'''
students = [
 {"name": "Alice", "score": 85},
 {"name": "Bob", "score": 72},
 {"name": "Charlie", "score": 91},
 {"name": "David", "score": 65},
]

merit = {i: s["name"] for i, s in enumerate(students) if s["score"] > 80}
passlist = [
    {
        "name": s["name"],
        "score": s["score"],
        "merit": "Pass" if s["score"] >= 70 else "Fail"
    }
    for s in students
]

print(passlist)


