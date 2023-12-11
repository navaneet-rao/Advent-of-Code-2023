from collections import defaultdict
import sys
file = open(sys.argv[1]).read().strip()
ans = 0
for line in file.split('\n'):
    first, rest = line.split('|')
    id_, card = first.split(':')
    card_nums = [int(x) for x in card.split()]
    rest_nums = [int(x) for x in rest.split()]
    # print(card_nums, rest_nums)
    val = len(set(card_nums) & set(rest_nums))
    if val > 0:
        ans += 2**(val - 1)
print(ans)