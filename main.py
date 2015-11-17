from ortoolpy import set_partition
import itertools
import sys

LOW_LIMIT = 5000
LOW_LIMIT2 = 3000
FILE_NAME = 'data.txt'

def convert2value(index):
    return values[index]

def calc_weight(combination):
    if sum(combination) > LOW_LIMIT:
        return sum(combination) - LOW_LIMIT
    elif sum(combination) > LOW_LIMIT2:
        return (sum(combination) - LOW_LIMIT2)
    else:
        return sys.maxint

def create_group(values):
    index_combinations = []
    group = []

    for i in range(1, len(values)+1):
        index_combinations.extend(list(itertools.combinations(range(len(values)), i)))
    print 'create ' + str(len(index_combinations)) + ' groups'

    for index_combination in index_combinations:
        elements_combination = map(convert2value, index_combination)
        group.append( [calc_weight(elements_combination), index_combination] )
    print 'finish calc weight'
    return group 

values = []
fh = open(FILE_NAME)
lines = fh.readlines()
for line in lines:
    values.append(int(line))
fh.close

print 'calc partition of a set for...'
print values

group = create_group(values)
indexs = set_partition(len(group), group)

print '=RESULT='

for index in indexs: 
    #print "weight:" + str(group[index][0])
    print ''.join(str(map(convert2value, group[index][1])))

