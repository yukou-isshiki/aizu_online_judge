a = [input() for i in range(2)]
start = int(a[0].split(" ")[1])
end = int(a[0].split(" ")[2])
word = a[1]
if start == end:
    print(word)
else:
    first_part = word[:start-1]
    middle_part = ''.join(list(reversed(word[start-1:end])))
    end_part = word[end:]
    print(f"{first_part}{middle_part}{end_part}")