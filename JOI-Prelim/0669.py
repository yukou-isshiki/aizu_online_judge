input_str_list = input().split(" ")
X = int(input_str_list[0])
L = int(input_str_list[1])
R = int(input_str_list[2])
if L == R:
    print(L)
else:
    diff = 100001
    number = 0
    for i in range(L, R+1):
        if abs(X-i) < diff:
            diff = abs(X-i)
            number = i
    print(number)