from collections import defaultdict
import re

# file = open("D:\\codes\\AOC2023\\DAY3\\sample.txt").read().strip()
file = open("D:\\codes\\AOC2023\\DAY3\\input-part1.txt").read().strip()
lines = file.split('\n')
G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])
ans = 0
for r in range(len(G)):
    nums = re.findall('-?\d+', lines[r])
    print(nums)
    n = 0
    neg = False
    has_part = False
    for c in range(len(G[r])+1):
        # if c<C and G[r][c]=='-':
        #     neg = True
        if c<C and G[r][c].isdigit():
            n = n*10+int(G[r][c])
            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0<=r+rr<R and 0<=c+cc<C:
                        ch = G[r+rr][c+cc]
                        if not ch.isdigit() and ch != ".":
                            has_part = True
        elif n>0 :
            neg = False
            if neg:
                n *= -1
            print (n, has_part)
            if has_part:
                ans += n
            n = 0
            has_part = False
            neg = False
        else:
            neg = False 
        if c<C and G[r][c]=='-':
            neg = True
print(ans)
            