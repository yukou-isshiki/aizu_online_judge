import sys
for l in sys.stdin:
    if l == "END OF INPUT\n":
        break
    else:
        word_list = l.replace("\n", "").split(" ")
        word_len_list = []
        for word in word_list:
            word_len_list.append(str(len(word)))
        output_data = "".join(word_len_list)
        print(output_data)