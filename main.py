from ortoolpy import set_partition
import itertools
import sys
import random

LOW_LIMIT = 5000
LOW_LIMIT2 = 3000
FILE_NAME = 'data.txt'

def calc_weight(combination):
    if sum(combination) > LOW_LIMIT:
        return sum(combination) - LOW_LIMIT
    elif sum(combination) > LOW_LIMIT2:
        return (sum(combination) - LOW_LIMIT2)*50
    else:
        return -1

def create_group(values):
    index_combinations = []
    group = []

    for i in range(1, len(values)+1):
        index_combinations.extend(list(itertools.combinations(range(len(values)), i)))
    print 'create ' + str(len(index_combinations)) + ' groups'

    lower_cut = 0
    upper_cut = 0
    for index_combination in index_combinations:
        elements_combination = map(lambda(i, e):e, filter(lambda(i,e):i in index_combination, enumerate(values)))
        weight = calc_weight(elements_combination)
        if weight < 0:
            lower_cut+=1
            continue
        if weight > 1000:
            upper_cut+=1
            continue
        group.append( [weight, index_combination] )
    print 'finish calc weight'
    print 'cut lower'
    print lower_cut
    print 'cut upper'
    print upper_cut
    print 'calc'
    print len(index_combinations) - lower_cut - upper_cut
    return group 

def calc_partition_of_a_set(values):
    print 'calc partition of a set for...'
    print values

    group = create_group(values)
    indexs = set_partition(len(group), group)

    print '=RESULT='

    for index in indexs: 
        #print "weight:" + str(group[index][0])
        result = map(lambda(i, e):e, filter(lambda(i,e):i in group[index][1], enumerate(values)))
        print ''.join(str(result))
        print 'sum:' + str(sum(result))
        print ''
    print ''


values = [[],[],[]]
fh = open(FILE_NAME)
lines = fh.readlines()
counter = 0
random.shuffle(lines)
for line in lines:
    values[counter%3].append(int(line))
    counter+=1
fh.close

calc_partition_of_a_set(values[0])
calc_partition_of_a_set(values[1])
calc_partition_of_a_set(values[2])

