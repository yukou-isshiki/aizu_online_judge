input_str_list = input().split(" ")
dict = {}
dict[1] = 0
dict[2] = 0
for input_str in input_str_list:
    if input_str == "1":
        dict[1] += 1
    else:
        dict[2] += 1
print(max(dict, key=dict.get))