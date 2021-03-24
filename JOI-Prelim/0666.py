import heapq

input_str_list = input().split(" ")
new_list = []
for input_str in input_str_list:
    new_list.append(int(input_str))
max_2nd_list = heapq.nlargest(2, new_list)
print(sum(max_2nd_list))