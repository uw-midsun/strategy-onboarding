import matplotlib.pyplot as plt


def plot_test_data():
    file = open('test_data.csv', 'r')
    fig = plt.figure(figsize=(6, 4))
    grid = plt.GridSpec(3, 2, hspace=0.3, wspace=0.2)
    ax1 = plt.subplot(grid[0, 0])
    ax2 = plt.subplot(grid[0, 1])
    ax3 = plt.subplot(grid[1, 0])
    ax4 = plt.subplot(grid[1, 1])
    ax5 = plt.subplot(grid[2, 0:])
    for index, line in enumerate(file):
        plot_vals = line.split(',')
        ax1.scatter(index, int(plot_vals[0]), 1)
        ax2.scatter(index, int(plot_vals[1]), 1)
        ax3.scatter(index, int(plot_vals[2]), 1)
        ax4.scatter(index, int(plot_vals[3]), 1)
        ax5.scatter(index, int(plot_vals[4]), 1)
    file.close()
    plt.show()
    pass

if __name__ == "__main__":
    plot_test_data()
