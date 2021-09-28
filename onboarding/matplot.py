'''
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

import pandas
import matplotlib.pyplot as plt
from math import log10


def main():
    content = []

    with open('test_data.csv') as f:
        content = f.readlines()

    # Split each line by comma, and parse strings to ints
    content = list(map(lambda x: map(int, x.strip().split(',')), content))

    # Transform the data by swapping rows and columns
    content = list(zip(*content))

    # Use scale so first three columns are comparable
    plt.yscale('log')

    # First three columns are in the same plot
    for i in content[1:-1]:
        plt.plot(content[0], i)

    plt.savefig("1-3.png")
    plt.clf()

    # Using built in logarithmic scaling doesn't work due to the large numbers
    # So the log of each term is manually calculated and then plotted linearly
    plt.yscale('linear')
    plt.ylabel("log(y)")

    plt.plot(content[0], list(map(log10, content[4])), label="line 4")

    plt.legend()
    plt.savefig("4.png")


if __name__ == "__main__":
    main()
