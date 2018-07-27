import csv
import matplotlib.pyplot as plt


awards_file = csv.reader(open("../award_amounts_files/nsf_awards_2017.txt"), delimiter="\n")

# turn awards file into a list of integers
award_list_text = [row[0] for row in awards_file]
award_list_int = [int(i) for i in award_list_text]

# all awards of $1 or less removed then sorted into a list
cleaned_awards = [i for i in award_list_int if i > 1]
sorted_awards = sorted(cleaned_awards, reverse=True)

# create an index to act as x variable in plot (hack)
index = list(range(len(sorted_awards)))

print(len(index)/2)
# 5785.5

first_half_awards = sorted_awards[:5786]
second_half_awards = sorted_awards[5786:]

first_half_index = index[:5786]
second_half_index = index[5786:]

# plot (x, y) as in (index, sorted_awards)
plt.plot(first_half_index, first_half_awards, lw=0)
plt.fill_between(first_half_index, first_half_awards, 0, facecolor='blue', alpha=0.5)

plt.plot(second_half_index, second_half_awards, lw=0)
plt.fill_between(second_half_index, second_half_awards, 0, facecolor='red', alpha=0.5)

# set y axis limit
axes = plt.gca()
axes.set_ylim([0, 5000000])
axes.set_xlim([0, 12000])


# view plot
plt.show()
