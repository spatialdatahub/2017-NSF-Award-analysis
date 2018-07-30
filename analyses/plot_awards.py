import csv
import numpy as np
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

#print(len(index)/2)
#print(len(index))
## 5785.5
#print(max(sorted_awards))
#print(min(sorted_awards))

# divide the awards list and index list in half
half = int(len(index)/2)

first_half_awards = sorted_awards[:half]
second_half_awards = sorted_awards[half:]

first_half_index = index[:half]
second_half_index = index[half:]

# divide the awards list and index list into 4/5 and 1/5, because the
# list lengthis divisible by 5 but not 4
fourfifths = int(len(index)/5)*4

four_fifths_awards = sorted_awards[:fourfifths]
one_fifth_awards = sorted_awards[fourfifths:]

four_fifths_index = index[:fourfifths]
one_fifth_index = index[fourfifths:]

# gather subplots for axis labels
fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)

fig.text(0.5, 0.04,
         'Grant index sorted from largest to smallest', ha='center')
fig.text(0.06, 0.5, 'Grant size in millions of dollars',
         va='center', rotation='vertical')

# top subplot
# plot (x, y) as in (index, sorted_awards)
plt.subplot(2, 1, 1)
plt.plot(first_half_index, first_half_awards, 'k-',
         lw=1, label='highly findable data', color='blue', alpha=0.5)
plt.fill_between(first_half_index, first_half_awards,
                 0, facecolor='blue', alpha=0.5)

plt.plot(second_half_index, second_half_awards, 'k-',
         lw=1, label='not highly findable data', color='red', alpha=0.5)
plt.fill_between(second_half_index, second_half_awards,
                 0, facecolor='red', alpha=0.5)

# turn off x tick marks
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

# set axis limits
axes = plt.gca()
axes.set_xlim([0, 12000])
axes.set_ylim([0, 5000000])

# set y axis ticks
y_tick_locs = [0, 1000000, 2000000, 3000000, 4000000, 5000000]
y_tick_labels = [0, 1, 2, 3, 4, 5]
plt.yticks(y_tick_locs, y_tick_labels)

# set x-axes tick marks
#x = [0, 3000, 6000, 9000, 12000]
#plt.xticks(range(min(x), max(x)+1, 3000))

# put legend into upper subplot
plt.legend(loc='upper right', edgecolor='w')

# put vertical line at 50 % mark on graph
plt.axvline(x=half, color='k', linestyle='--', lw=1)


# make title
plt.title('NSF research grants awarded in 2017')

# make text describing y axis
grant_size_string="""To see smaller sized grant more clearly
the y axis stops at $5 million, but the
largest grant was over $ 209 million"""

plt.text(500,4500000, grant_size_string, verticalalignment='top')

# bottom subplot
plt.subplot(2, 1, 2)
plt.plot(four_fifths_index, four_fifths_awards, 'k-',
         lw=1, color='blue', alpha=0.5)
plt.fill_between(four_fifths_index, four_fifths_awards,
                 0, facecolor='blue', alpha=0.5)

plt.plot(one_fifth_index, one_fifth_awards, 'k-',
         lw=1, color='red', alpha=0.5)
plt.fill_between(one_fifth_index, one_fifth_awards,
                 0, facecolor='red', alpha=0.5)

# set axis limits
axes = plt.gca()
axes.set_xlim([0, 12000])
axes.set_ylim([0, 5000000])

# set y axis ticks
y_tick_locs = [0, 1000000, 2000000, 3000000, 4000000, 5000000]
y_tick_labels = [0, 1, 2, 3, 4, 5]
plt.yticks(y_tick_locs, y_tick_labels)

#plt.xticks(range(min(x), max(x)+1, 3000))

# set x-axes tick marks
#x = [0, 3000, 6000, 9000, 12000]
#plt.xticks(range(min(x), max(x)+1, 3000))

# turn off x tick marks
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

plt.axvline(x=fourfifths, color='k', linestyle='--', lw=1)

plt.annotate("", xy=(fourfifths, 1500000), xytext=(half, 1500000),
             arrowprops=dict(arrowstyle="->"))

arrow_text = """Spatial Data Hub will increase
the number of grants with
highly findable data"""

plt.text(half, 3500000, arrow_text, fontsize=10, verticalalignment='top')



#
# view plot
plt.show()
