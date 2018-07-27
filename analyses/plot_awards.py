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
# 5785

# plot (x, y) as in (index, sorted_awards)
plt.plot(index, sorted_awards)
plt.fill_between(index, sorted_awards, 0, color='yellow')

# fill in area under the plot

# view plot
plt.show()
