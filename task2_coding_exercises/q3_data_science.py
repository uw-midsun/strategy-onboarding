"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""

# Your code here
import matplotlib.pyplot as plt
import csv

var1 = []
var2 = []
var3 = []
var4 = []
var5 = []

with open('q3_test_data.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        var1.append(row[0])
        var2.append(row[1])
        var3.append(row[2])
        var4.append(row[3])
        var5.append(row[4])

plt.plot(var1, var2, color='r', linestyle='dotted',
         marker='.', label="Plot 1")
plt.plot(var1, var3, color='g', linestyle='dotted',
         marker='x', label="Plot 2")
plt.plot(var1, var4, color='b', linestyle='dotted',
         marker='^', label="Plot 3")
plt.plot(var1, var5, color='y', linestyle='dotted',
         marker='1', label="Plot 4")

plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.title('Q3 Test Data Plot', fontsize=20)
plt.grid()
plt.legend()
plt.show()
