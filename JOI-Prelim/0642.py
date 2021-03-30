a = [input() for i in range(2)]
board_list = a[1].split(" ")
count = 1
most_count = 1
for board in board_list:
    if board == "0":
        most_count = max(most_count, count)
        count = 1
    else:
        count += 1
most_count = max(most_count, count)
print(most_count)