science = [int(input()) for i in range(4)]
social = [int(input()) for j in range(2)]
science2 = sorted(science, reverse=True)
social2 = sorted(social, reverse=True)
science2.pop(-1)
social2.pop(-1)
result = sum(science2) + sum(social2)
print(result)