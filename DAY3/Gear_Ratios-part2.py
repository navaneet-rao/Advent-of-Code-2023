from collections import defaultdict
import re

file = open("D:\\codes\\AOC2023\\DAY3\\input-part1.txt").read().strip()
# file = open("D:\\codes\\AOC2023\\DAY3\\input-part1.txt").read().strip()

lines = file.split('\n')
G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])
ans = 0
nums = defaultdict(list)
for r in range(len(G)):
    gears = set()
    # nums = re.findall('-?\d+', lines[r])
    print(nums)
    n = 0
    neg = False
    has_part = False
    for c in range(len(G[r])+1):
        if c<C and G[r][c].isdigit():
            n = n*10+int(G[r][c])
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0<=r+rr<R and 0<=c+cc<C:
                        ch = G[r+rr][c+cc]
                        if not ch.isdigit() and ch != ".":
                            has_part = True
                        if ch == '*':
                            gears.add((r+rr, c+cc))
        elif n>0 :
            for gear in gears :
                nums[gear].append(n)
            neg = False
            if neg:
                n *= -1
            print (n, has_part)
            if has_part:
                ans += n
            n = 0
            has_part = False
            neg = False
            gears = set()
        else:
            neg = False 
        if c<C and G[r][c]=='-':
            neg = True
print(ans)
print(nums)
ans = 0   
for k,v in nums.items():
    if len(v)==2:
        ans += v[0]*v[1]
print(ans)