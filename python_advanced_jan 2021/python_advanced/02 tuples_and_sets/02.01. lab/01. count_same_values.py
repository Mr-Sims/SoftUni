# tt = tuple(input().split(" "))
# occurances = []

# for i in range(len(tt)):
#     if tt[i] in occurances:
#         continue
#     else:
#         print(f"{float(tt[i])} - {tt.count(tt[i])} times")
#         occurances.append(tt[i])


################################################################
############# Решение от LAB-A ################################

numbers = tuple(map(float, input().split()))

nums_and_occurances = {}
for num in numbers:
    if num not in nums_and_occurances:
        nums_and_occurances[num] = 0
    nums_and_occurances[num] += 1

[print(f"{key} - {value} times") for key, value in nums_and_occurances.items()]

