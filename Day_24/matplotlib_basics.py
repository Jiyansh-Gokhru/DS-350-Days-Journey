import matplotlib.pyplot as plt

# Dummy data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Line Plot
plt.figure()
plt.plot(x, y, label="Line Plot")
plt.title("Line Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid()
plt.show()

# Bar Chart
plt.figure()
plt.bar(x, y, label="Bar Chart")
plt.title("Bar Chart Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid()
plt.show()

# Histogram
plt.figure()
plt.hist(y, bins=5, label="Histogram")
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()
plt.grid()
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(x, y, label="Scatter Plot")
plt.title("Scatter Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid()
plt.show()
