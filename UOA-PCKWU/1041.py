import sys
a = []
i = 0
limit = 0
sum = 0
for l in sys.stdin:
    if i == 0:
        limit = int(l) // 4
        i += 1
    elif i == limit:
        sum += int(l)
        print(sum)
        sum = 0
        i = 0
        limit = 0
    else:
        sum += int(l)
        i += 1