import csv


"""This document contains code for exploratory statistics that describe the awards data.
because the awards data is simply a list of grant amounts I will not be doing any in depth
analyses of who or why these awards have been granted."""

# get data from file
awards_file = csv.reader(open("./award_amounts_files/nsf_awards_2017.txt"), delimiter="\n")

# turn awards file into a list of integers
award_list_text = [row[0] for row in awards_file]
award_list_int = [int(i) for i in award_list_text]

# all awards of $10 or less removed then sorted into a list
cleaned_awards = [i for i in award_list_int if i > 10]
sorted_awards = sorted(cleaned_awards, reverse=True)

# create an index to act as x variable in plot (hack)
index = list(range(len(sorted_awards)))

######################################################
# this analysis pertains to awards above $10 in size #
######################################################


# total number of awards
number_of_grants = len(sorted_awards)
print(number_of_grants)

# total amount of money awarded
total_amount_awarded = sum(sorted_awards)
print(total_amount_awarded)
print('1000000000 is one billion')
print('1000000 is one million')

# count of 20 % of awards
count_twenty_percent=int(number_of_grants*0.2)
print(count_twenty_percent)

# count of 80 % of awards
count_eighty_percent=int(number_of_grants*0.8)
print(count_eighty_percent)

# amount of money in largest 20 % of awards



# of awards holding 20 % of the value

# 20 % of total value

# of awards holding 80 % of the value

# 80 % of the total value
