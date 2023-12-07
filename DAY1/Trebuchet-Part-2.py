file = open('D:\\codes\\AOC2023\\DAY1\\input-part2.txt', 'r')
ans = 0
total_ans = 0
lines = file.readlines()
y = []
for x in lines:
    y.append(x.strip())
print(y)

for line in y:
    digits = []
    print(line)
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        # print(digits)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                digits.append(str(d+1))
    ans = int(digits[0]+digits[-1])
    total_ans += ans 
print(total_ans)