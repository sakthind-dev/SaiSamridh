## Linear Regression in Python

'''
1. Create a pandas DataFrame – to organize and display tabular data.
2. Print and summarize the data – using built-in pandas functions.
3. Visualize data with a scatter plot – using matplotlib.
4. Fit a simple linear regression – with scikit-learn, and plot the regression line.
'''

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Create sample data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David','Ram', 'Anjen','Gana','Murug','Sakthi'],
    'Age': [25, 30, 22, 35,56,67,89,90,90],
    'Score': [85, 90, 88, 95,90,90,90,90,91]
})

# Print the DataFrame
print(data)
# Summarize the data
print(data.describe())

# Visualize the data with a scatter plot
plt.scatter(data['Age'], data['Score'])
plt.xlabel('Age')
plt.ylabel('Score')
plt.title('Age vs Score')
plt.show()

#print("matplotlib installed:", plt.__version__)

# Fit a simple linear regression
X = data['Age'].values.reshape(-1, 1)  # Reshape for sklearn
y = data['Score'].values
model = LinearRegression()
model.fit(X, y)

# Plot the regression line
plt.scatter(data['Age'], data['Score'], color='blue')
plt.plot(data['Age'], model.predict(X), color='red')
plt.xlabel('Age')
plt.ylabel('Score')
plt.title('Age vs Score with Regression Line')
plt.show()

# Print the coefficients of the linear regression
print(f'Coefficient: {model.coef_[0]}')
print(f'Intercept: {model.intercept_}')

# Prepare data for regression
X = data[['Age']]
y = data['Score']
model = LinearRegression()
model.fit(X, y)

# Make predictions for plotting
x_vals = np.linspace(data['Age'].min(), data['Age'].max(), 100).reshape(-1, 1)
# Convert to DataFrame with the correct column name
x_vals_df = pd.DataFrame(x_vals, columns=['Age'])
y_preds = model.predict(x_vals_df)

# Plot
plt.figure(figsize=(8, 5))
plt.scatter(data['Age'], data['Score'], color='red', label='Data Points')
plt.plot(x_vals_df, y_preds, color='blue', label='Regression Line')
plt.title('Score vs Age')
plt.xlabel('Age')
plt.ylabel('Score')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
plt.plot([23,35,78,90,64], color='red', marker='o', label='PSeries')
plt.xlabel('Population')
plt.ylabel('Total count')
plt.title('Population Growth')
plt.legend()

plt.style.use('seaborn-v0_8') # You can try other styles like 'ggplot', 'fivethirtyeight', 'dark_background', etc.
# You can also list available styles with `print(plt.style.available)`

print(plt.style.available)
plt.savefig('my_plot.png')
print('Plot saved as my_plot.png')

#California housing dataset analysis 
# The California housing dataset is a popular dataset used for regression tasks. 
# It contains information about various features of houses in California, such as median income, 
# median house value, total rooms, total bedrooms, population, households, latitude, and longitude. 
# The target variable is typically the median house value.
import pandas as pd

# Load the california_housing_train.csv dataset into a DataFrame
california_df = pd.read_csv('california_housing_train.csv')
# Display the first 5 rows of the DataFrame
print(california_df.head())

# Calculate and display summary statistics
print(california_df.describe())

#histogram of 'median_house_value'
plt.figure(figsize=(10, 6))
plt.hist(california_df['median_house_value'], bins=50, edgecolor='black')
plt.title('Distribution of Median House Value')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

#scatter plot of 'median_income' vs 'median_house_value'
plt.figure(figsize=(10, 6))
plt.scatter(california_df['median_income'], california_df['median_house_value'], alpha=0.5)
plt.title('Median Income vs. Median House Value')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.grid(True)
plt.show()

# Group by 'housing_median_age' and calculate the mean for each group
mean_by_age = california_df.groupby('housing_median_age').mean()

# Display the resulting DataFrame
print(mean_by_age.head())

#plot the mean median house value against housing median age
plt.figure(figsize=(12, 7))
plt.plot(mean_by_age.index, mean_by_age['median_house_value'], marker='o', linestyle='-')
plt.title('Mean Median House Value vs. Housing Median Age')
plt.xlabel('Housing Median Age')
plt.ylabel('Mean Median House Value')
plt.grid(True)
plt.show()

#calculate the correlation between 'median_income' and 'median_house_value'
correlation = california_df['median_income'].corr(california_df['median_house_value'])
print(f"Correlation between median_income and median_house_value: {correlation:.2f}")

#scatter plot of 'total_rooms' vs 'median_house_value'
plt.figure(figsize=(10, 6))
plt.scatter(california_df['total_rooms'], california_df['median_house_value'], alpha=0.5)
plt.title('Total Rooms vs. Median House Value')
plt.xlabel('Total Rooms')
plt.ylabel('Median House Value')
plt.grid(True)
plt.show()

#linear regression using 'median_income' to predict 'median_house_value'
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Prepare the data
X = california_df[['median_income']]
y = california_df['median_house_value']

# Split the data into training and testing sets (optional but good practice)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Display model coefficients
print(f"Coefficient (median_income): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, alpha=0.5, label='Actual Values')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.title('Linear Regression: Median Income vs. Median House Value')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.legend()
plt.grid(True)
plt.show()
