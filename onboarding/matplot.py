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
    figure, axis = plt.subplots(2, 2)

    for row in content:
        x = row[0]
        axis[0, 0].scatter(int(x), int(row[1]))
        axis[0, 1].scatter(int(x), int(row[2]))
        axis[1, 0].scatter(int(x), int(row[3]))
        axis[1, 1].scatter(int(x), int(row[4]))

plt.show()
