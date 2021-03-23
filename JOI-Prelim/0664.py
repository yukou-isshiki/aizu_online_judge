count = 0
a = [input() for i in range(2)]
word = a[1]
for i in range(len(word)):
    if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
        count += 1
print(count)