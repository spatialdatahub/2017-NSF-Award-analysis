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
#print(number_of_grants)

# total amount of money awarded
total_amount_awarded = sum(sorted_awards)
#print(total_amount_awarded)
#print('1000000000 is one billion')
#print('1000000 is one million')

# count of 20 % of awards
#count_twenty_percent=int(number_of_grants*0.2)
#print(count_twenty_percent)

# count of 80 % of awards
#count_eighty_percent=int(number_of_grants*0.8)
#print(count_eighty_percent)

# amount of money in largest 20 % of awards
##### first, sort largest to smallest, then extract
#largest_20_percent_of_awards =  sorted_awards[:count_twenty_percent]

##### the largest 20 % and get the sum
#largest_20_percent_of_awards_amount = sum(largest_20_percent_of_awards)
#print("The sum of the largest 20 % of awards is: $ {}.".format(largest_20_percent_of_awards_amount))

# amount of money in smallest 80 % of awards
##### first, sort largest to smallest, then extract
#smallest_80_percent_of_awards =  sorted_awards[count_eighty_percent:]

##### the largest 20 % and get the sum
#smallest_80_percent_of_awards_amount = sum(smallest_80_percent_of_awards)
#print("The sum of the smallest 80 % of awards is: $ {}.".format(smallest_80_percent_of_awards_amount))


# of awards holding 20 % of the value

# 20 % of total value
# is this that important of a measure?
#twenty_percent_of_value=int(total_amount_awarded*0.2)
#twenty_percent_of_value_string="""Twenty percent of the total award value is $ {}, and it is being held"""
#print("Twenty percent of the total award value is $ {}.".format(twenty_percent_of_value))

# 80 % of the total value
eighty_percent_of_value=int(total_amount_awarded*0.8)

# of awards holding 80 % of the value
# there must be a good way to do this... I can probably code a loop that will make it happen
#acc = 0
#count = 0
#for i in sorted_awards:
#    acc + i 
#    count + 1 
#    if acc > eighty_percent_of_value:
#        print(acc)
#        #break
#print(acc)
#print(count)

#def how_many_hold_80_percent(cur, acc):
#    # base case
#    # return final state
#    if cur == 15:
#        return acc
#
#    # recursive case
#    else:
#        return how_many_hold_80_percent(cur + 1, acc + cur)
#
#print(how_many_hold_80_percent(1,0))
#
#def list_sum_recursive(input_list):
#    if input_list == []:
#        return 0
#    else:
#        head = input_list[0]
#        smaller_list = input_list[1:]
#        return head + list_sum_recursive(smaller_list)
#
#print(list_sum_recursive(sorted_awards))

def accumulator_if(l, s):
    """This is definitely not perfect... but it kinda works"""
    a = 0
    c = 0
    for i in l:
        if a < s:
            c = c + 1 
            a = a + i 
        else:
            break
    return {'value': a, 'count': c, 'stop-value': s}



res = accumulator_if(sorted_awards, eighty_percent_of_value)

print(res['value'] / total_amount_awarded)
print(res['count'] / number_of_grants)

#return_count_for_greatest_80_percent(sorted_awards, eighty_percent_of_value)

#eighty_percent_of_value_string="""Eighty percent of the total award value is $ {0}, and it is being held by the top {1} % of the grants""".format(eighty_percent_of_value, 'HEY')
#print(eighty_percent_of_value_string)
