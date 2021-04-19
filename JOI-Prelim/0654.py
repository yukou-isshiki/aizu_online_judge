input_list = [input() for i in range(2)]
stump_string = input_list[1]
string1 = ""
count = 0
for i in range(len(stump_string)):
    string = stump_string[i]
    if string1 == "":
        string1 = string
    else:
        if string != string1:
            count += 1
            string1 = ""
        else:
            string1 = string
print(count)