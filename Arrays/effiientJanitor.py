# HackerRank: Efficient Janitor

# The janitor at Hacker High School is insanely efficient. By end of each day,
# all of the waste from the trash cans in the school has been shifted into
# plastic bags which can carry waste weighing between 1.01 lbs and 3.00 lbs.
# All of the plastic bags must be dumped into the trash cans outside the school.
#
# The janitor can carry at most 3.00 lbs at once. One trip is described
# as selecting a few bags which together don't weigh more than 3.00 lbs,
# dumping them in the outdoor trash can and returning to the school. The
# janitor wants to make minimum # of trips to the outdoor trash can.

# Given the number of plastic bags, n, and the weights of each bag, determine
# the minimum number of trips if the janitor selects bags in the optimal way.
# For example, given n = 5 plastic bags weighing  weight = [1.01, 1.99, 2.5, 1.5, 1.01],
# the janitor can carry all of the trash out in 3 trips: [1.01 + 1.99 , 2.5, 1.5 + 1.01].

# Function Description:
# Complete the function efficient_janitor in the editor below. The function must return
# a single int that represents the minimum number of trips to be made.
# efficientJanitor has the following parameter(s):
# weight[weight[0], ..., weight[n-1]]: an array of floating-point ints


def efficientJanitor(weight):
    max_weight = 3
    rem_dict = initDict(weight, max_weight)
    calcBins(weight, rem_dict)
    return calcResults(rem_dict, max_weight)


def initDict(weight, max_weight):
    rem_dict = {i: max_weight for i in range(len(weight))}
    return rem_dict


def calcBins(weight, rem_dict):
    for i in range(len(weight)):
        for k in rem_dict.keys():
            if weight[i] <= rem_dict[k]:
                rem_dict[k] -= weight[i]
                break

def calcResults(rem_dict, max_weight):
    results = 0
    for value in rem_dict.values():
        if value != max_weight:
            results += 1
    return results


weight = [1.01, 1.99, 2.5, 1.5, 1.01]
weight2 = [1.5, 1.5, 1.5, 1.5, 1.5]
weight3 = [1.5, 1.5, 1.5, 1.5]
print(efficientJanitor(weight3))
