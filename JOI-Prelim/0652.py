input_list = input().split(" ")
login_bonus = int(input_list[0])
week_bonus = int(input_list[1])
min_coin = int(input_list[2])
day_count = 1
coin_count = 0
for i in range(1, min_coin+1):
    coin_count += login_bonus
    if i % 7 == 0:
        coin_count += week_bonus
    if min_coin <= coin_count:
        break
    else:
        day_count += 1
print(day_count)

"""
for i in range(min_coin+1):
    coin_count += login_bonus
    if week_day == 7:
        coin_count += week_bonus
        day_count += 1
        week_day = 1
    else:
        day_count += 1
        week_day += 1
    if min_coin <= coin_count:
        break
print(day_count)
"""