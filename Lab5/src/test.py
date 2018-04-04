# import sys
# import math

# res = []
# n = raw_input()
input = []
while True:
    line = raw_input()
    if not line:
        break
    input.append(int(line))

i = 0
while i < len(input):
    res = []
    for j in range(i+1, i+1+input[i]):
        res.append(input[j])
    i += 1+input[i]
    re = 0
    cur = 0
    while re < len(res):
        re += 1
        if res[cur] == 0:
            res.pop(cur)
            res.append(0)
        else:
            cur += 1
    for num in res:
        print num
