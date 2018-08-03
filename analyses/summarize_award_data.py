import csv
from tabulate import tabulate


"""
This document contains code for exploratory statistics that describe the awards data.
because the awards data is simply a list of grant amounts I will not be doing any in depth
analyses of who or why these awards have been granted.

I want to know how much money the top 50 % of awards are worth
I want to know how many grants hold 50 % of the money
I want to know the number of grants below a certain size

What would I want a table from this to look like?
Should it be quartiles?
This table doesn't really explain much.

item       25%         50%        75%        100% 
---------  ----------  ---------  ---------  ---------
# grants   # count     # count    # count    # count
$ total    $ total     $ total    $ total    $ total

How about this statement:
The top 50 % of the total amount granted are held by ## % of the awards.
The top 80 % of the total amount granted are held by ## % of the awards.


"""

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


def accumulator_if(l, stop):
    "l is the list and stop is the stop value for the sum of the values in the list."
    acc = 0
    count = 0

    for i in l:
        if acc + i > stop:
            break
        else:
            count = count + 1 
            acc = acc + i 

    return {'value': acc, 'count': count, 'stop-value': stop}



######################################################
# this analysis pertains to awards above $10 in size #
######################################################


# total number of awards
number_of_grants = len(sorted_awards)

# total amount of money awarded
total_amount_awarded = sum(sorted_awards)

# count of 20 % of awards
count_twenty_percent=int(number_of_grants*0.2)

# count of 25 % of awards
count_twenty_five_percent=int(number_of_grants*0.25)

# count of 50 % of awards
count_fifty_percent=int(number_of_grants*0.5)

# count of 75 % of awards
count_seventy_five_percent=int(number_of_grants*0.75)

# count of 80 % of awards
count_eighty_percent=int(number_of_grants*0.8)



# amount of money in largest 20 % of awards
##### first, sort largest to smallest, then extract
largest_20_percent_of_awards =  sorted_awards[:count_twenty_percent]

##### the largest 20 % and get the sum
largest_20_percent_of_awards_amount = sum(largest_20_percent_of_awards)

# amount of money in smallest 80 % of awards
##### first, sort largest to smallest, then extract
smallest_80_percent_of_awards =  sorted_awards[count_eighty_percent:]

##### the largest 20 % and get the sum
smallest_80_percent_of_awards_amount = sum(smallest_80_percent_of_awards)

# of awards holding 20 % of the value

# 20 % of total value
# is this that important of a measure?
#twenty_percent_of_value=int(total_amount_awarded*0.2)
#twenty_percent_of_value_string="""Twenty percent of the total award value is $ {}, and it is being held"""
#print("Twenty percent of the total award value is $ {}.".format(twenty_percent_of_value))

# 80 % of the total value
eighty_percent_of_value=int(total_amount_awarded*0.8)

# number of awards holding 80 % of the value

# use accumulator definitaion to get the count and sum of the values in the list
# that add up to just less than 80 % of the total amount awarded.
res = accumulator_if(sorted_awards, eighty_percent_of_value)

print(res['stop-value'] - res['value'])
print(res['value']/res['stop-value'])
print(res['value']/total_amount_awarded)

eighty_percent_string = """Eighty percent of the total award value is ${0}, and it is being held by the top {1} grants, or the top {2} of grants.""".format(
    eighty_percent_of_value,
    res['count'],
    res['count']/number_of_grants)

print(eighty_percent_string)



# smoke test
smoke_headers = ["City", "State", "Country"] 

smoke_values = [("Indio", "California", "USA"),
                ("Riverside", "California", "USA"),
                ("Honolulu", "Hawaii", "USA"),
                ("Bremen", "Bremen", "Germany")]

#print(tabulate(smoke_values, smoke_headers))

print('\n')
# real table
# is this table helpful to anything? not really
table_headers = ["Item", "25%", "50%", "75%", "100%"]

table_values = [
    ("Award count", count_twenty_five_percent, count_fifty_percent, count_seventy_five_percent, number_of_grants),
    ("$ of total", total_amount_awarded*0.25, total_amount_awarded*0.5, total_amount_awarded*0.75, total_amount_awarded)
]


print(tabulate(table_values, table_headers))
"""
# total number of awards
number_of_grants = len(sorted_awards)

# total amount of money awarded
total_amount_awarded = sum(sorted_awards)

# count of 20 % of awards
count_twenty_percent=int(number_of_grants*0.2)

# count of 25 % of awards
count_twenty_five_percent=int(number_of_grants*0.25)

"""
