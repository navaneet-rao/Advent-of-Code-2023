from collections import defaultdict

file = open("D:\\codes\\AOC2023\\DAY2\\input-part1.txt").read().strip()
ans = 0
for line in file.split('\n'):
    # print(line)
    _id, line = line.split(':')
    V = defaultdict(int)
    for event in line.split(';'):
        # print(event)
        for balls in event.split(','):
            # print(balls)
            n, color = balls.split()
            n = int(n)
            print(n,color)    
            V[color] = max(V[color], n)       
    print(V)
    score = 1
    for v in V.values():
        score *= v
        print(score)
    ans += score
print('the total score is:', ans)
        