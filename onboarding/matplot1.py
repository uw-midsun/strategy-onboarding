import pandas as pd
import matplotlib.pyplot as plt

# Read in the csv file
df = pd.read_csv('test_data.csv', header = None)

# Plot and display legend
# b = blue, r = red
# . = small dot, -- = dashed line
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot(df[0], df[1], 'b--', label = 'Data 1')
plt.plot(df[0], df[2], 'r.', label = 'Data 2')
plt.legend()

# Set title and axis labels
plt.title('Sample Data')
plt.xlabel('Time')
plt.ylabel('Speed')

# Overlay grid
plt.grid()

# Set Viewing Rectangle
plt.xlim(0, 1000)
plt.ylim(0, 2000)

plt.show()

# these ones are very big data and messes with my computer
# plt.plot(df[0], df[4])
plt.plot(df[0], df[3])
plt.show()