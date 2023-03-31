# Python plottask
# Author: Anthony Mc Garry

import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution
mu, sigma = 5, 2
values = np.random.normal(mu, sigma, 1000)

# Create the histogram
num_bins = 50

fig, ax = plt.subplots()

n, bins, patches = ax.hist(values, num_bins, density=1, alpha=0.7, label='Normal Distribution')

# Add a title and axis labels to the plot
ax.set_title('Histogram of a Normal Distribution and h(x)=x^3')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

# Add a best fit line to the histogram
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--', label='Best Fit Line')
ax.set_ylim(top=np.max(y) * 1.05)

# Create the plot of the function h(x)=x^3
x = np.linspace(0, 10, 1000)
y = x ** 3
ax2 = ax.twinx()
ax2.plot(x, y, color='red')

# Add a legend to the plot
ax.legend()

# Display the plot
plt.show()