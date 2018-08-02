import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# get data from file
awards_file = csv.reader(open("../award_amounts_files/nsf_awards_2017.txt"), delimiter="\n")

# turn awards file into a list of integers
award_list_text = [row[0] for row in awards_file]
award_list_int = [int(i) for i in award_list_text]

# all awards of $10 or less removed then sorted into a list
cleaned_awards = [i for i in award_list_int if i > 10]
sorted_awards = sorted(cleaned_awards, reverse=True)

# create an index to act as x variable in plot (hack)
index = list(range(len(sorted_awards)))

# start with a histogram
num_bins = 50

#fig, ax = plt.subplots()

# the histogram of the data
#n, bins, patches = ax.hist(cleaned_awards, num_bins, density=1)
#
#ax.plot(bins)
#fig.tight_layout()
#plt.show()
ax = plt.axes()
ax.set_axisbelow(True)
ax.yaxis.grid(True)
#ax = plt.gca()
#ax.grid(True, zorder=0)

plt.hist(sorted_awards, bins=50, range=(0, 2500000),
        rwidth=0.5, color='#1A7C49')




plt.show()
