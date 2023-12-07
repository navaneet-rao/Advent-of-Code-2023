file = open('D:\\codes\\AOC2023\\DAY1\\input.txt', 'r')
lines = file.readlines()

y = []
for x in lines:
    y.append(x.strip())

print(y)

res = []
second_res = []
third_res = []
new_res = []
add = 0
total_add = 0
print()


for a in y:
    print(a)
    for i, v in enumerate(a):
        # print(v)
        res.append(v)
    print(res)
    second_res = res
    res = []
    for i in second_res:
        if i.isnumeric():
            new_res.append(int(i))
    print(new_res)
    third_res = new_res
    new_res = []
    empty_delimiter = ''
    add = add + int(empty_delimiter.join(map(str, [third_res[0], third_res[-1]])))
    total_add = add
    print(add)
    
print("total sun is :",total_add)