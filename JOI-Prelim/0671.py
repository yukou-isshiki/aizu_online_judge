a = [input() for i in range(2)]
num_list = a[1].split(" ")
count = 0
most_count = 0
before = 0
for num_str in num_list:
    num = int(num_str)
    if num < before:
        before = num
        most_count = max(count, most_count)
        count = 1
    else:
        count += 1
        before = num
most_count = max(count, most_count)
print(most_count)