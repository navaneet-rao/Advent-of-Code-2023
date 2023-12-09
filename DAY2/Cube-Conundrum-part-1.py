file = open("D:\\codes\\AOC2023\\DAY2\\input-part1.txt").read().strip()
ans = 0
for line in file.split('\n'):
    ok = True
    # print(line)
    _id, line = line.split(':')
    for event in line.split(';'):
        # print(event)
        for balls in event.split(','):
            # print(balls)
            n, color = balls.split()
            print(n,color)           
            if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                ok = False
    if ok:
        ans += int(_id.split()[-1])
        print(_id)
print(ans)
        