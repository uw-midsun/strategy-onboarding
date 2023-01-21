'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''
import matplotlib.pyplot as plt
import csv

with open('test_data.csv') as csv_file:
    content = csv.reader(csv_file)
    for row in content:
        print(row)
        x = row[0]
        for i in range(1, 4):
            plt.scatter(x, row[i])

plt.show()
