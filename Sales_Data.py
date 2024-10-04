import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [12000, 15000, 13000, 18000, 21000, 16000, 20000, 22000, 25000, 23000, 24000, 27000]
expenses = [7000, 8000, 7500, 9000, 9500, 8000, 10000, 11000, 12000, 11500, 11800, 13000]
units_sold = [500, 650, 550, 750, 850, 700, 800, 900, 1000, 950, 1100, 1200]

# 1. Line Plot for Revenue over Months
plt.figure(figsize=(10, 6))
plt.plot(months, revenue, label='Revenue', color='red', marker='o')  # Line plot
plt.xlabel('Months')  # X axis label
plt.ylabel('Revenue ($)')  # Y axis label
plt.title('Monthly Revenue')  # Title
plt.grid(True)  # Add gridlines
plt.legend()  # Add legend
plt.show()

# 2. Scatter Plot for Units Sold vs. Revenue
plt.figure(figsize=(10, 6))
plt.scatter(units_sold, revenue, color='green')  # Scatter plot
plt.xlabel('Units Sold')  # X axis label
plt.ylabel('Revenue ($)')  # Y axis label
plt.title('Units Sold vs. Revenue')  # Title
plt.grid(True)  # Add gridlines
plt.show()

# 3. Bar Chart for Revenue and Expenses Comparison
width = 0.4  # Width of the bars
x = np.arange(len(months))  # the label locations

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, revenue, width, label='Revenue', color='blue')  # Bar for revenue
plt.bar(x + width/2, expenses, width, label='Expenses', color='red')  # Bar for expenses
plt.xlabel('Months')  # X axis label
plt.ylabel('Amount ($)')  # Y axis label
plt.title('Revenue vs Expenses per Month')  # Title
plt.xticks(x, months)  # Set the x-ticks to be the months
plt.legend()  # Add legend   
plt.grid(True)  # Add gridlines
plt.show()

# 4. Histogram of Units Sold
plt.figure(figsize=(10, 6))
plt.hist(units_sold, bins=5, color='purple')  # Histogram
plt.xlabel('Units Sold')  # X axis label
plt.ylabel('Frequency')  # Y axis label
plt.title('Distribution of Units Sold')  # Title
plt.grid(True)  # Add gridlines
plt.show()
