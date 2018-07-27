import csv
import numpy as np
import matplotlib.pyplot as plt


awards_file = csv.reader(open("../award_amounts_files/nsf_awards_2017.txt"), delimiter="\n")

# turn awards file into a list of integers
award_list_text = [row[0] for row in awards_file]
award_list_int = [int(i) for i in award_list_text]

# all awards of $1 or less removed then sorted into a list
cleaned_awards = [i for i in award_list_int if i > 9]
sorted_awards = sorted(cleaned_awards, reverse=True)

# create an index to act as x variable in plot (hack)
index = list(range(len(sorted_awards)))

print(len(index)/2)
print(len(index))
# 5785.5
print(max(sorted_awards))
print(min(sorted_awards))

half_of_awards = int(len(index)/2)

first_half_awards = sorted_awards[:half_of_awards]
second_half_awards = sorted_awards[half_of_awards:]

first_half_index = index[:half_of_awards]
second_half_index = index[half_of_awards:]

# plot (x, y) as in (index, sorted_awards)
plt.plot(first_half_index, first_half_awards, 'k-', lw=0.5)
plt.fill_between(first_half_index, first_half_awards, 0, facecolor='blue', alpha=0.5)

plt.plot(second_half_index, second_half_awards, 'k-', lw=0.5)
plt.fill_between(second_half_index, second_half_awards, 0, facecolor='red', alpha=0.5)

# set axis limits
axes = plt.gca()
axes.set_xlim([0, 12000])
axes.set_ylim([0, 5000000])

# set x-axes tick marks
x = [0, 3000, 6000, 9000, 12000]
plt.xticks(range(min(x), max(x), 3000))

# x axis label
plt.xlabel('Grant index sorted from largest to smallest')

# y axis label
plt.ylabel('Grant size ($)')

# make title
plt.title('2017 NSF research grants awarded')

# make text box explaining plot
big=sum(first_half_awards)
small=sum(second_half_awards)

textstra="""The y axis on this graph terminates
at $5 million, but the largest grant
was actually over $200 million. The
sum of the largest 50% of grants is
${0} and the smallest 50%
of grants is ${1}.""".format(big, small)

textstr="""The y axis on this graph terminates
at $5 million, but the largest grant
was over $209 million."""


props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.text(5876, 4500000, textstr, fontsize=12, verticalalignment='top',bbox=props)

# view plot
plt.show()
