from collections import defaultdict
import sys
file = open(sys.argv[1]).read().strip()
ans = 0
N = defaultdict(int)
for i,line in enumerate(file.split('\n')):
    # print(i, line)
    N[i] += 1
    first, rest = line.split('|')
    id_, card = first.split(':')
    card_nums = [int(x) for x in card.split()]
    rest_nums = [int(x) for x in rest.split()]
    # print(card_nums, rest_nums)
    val = len(set(card_nums) & set(rest_nums))
    for j in range(val):
        # print(N)
        N[i+1+j] += N[i]
print(N.values())
print(sum(N.values()))