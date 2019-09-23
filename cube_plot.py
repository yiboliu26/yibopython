import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [ x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.summer, edgecolor='none', s=40)
plt.title("Cube Numbers", fontsize=25)
plt.xlabel("Value", fontsize=15)
plt.ylabel("Cube of Value", fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.show()
