race = [int(el) for el in input().split()]
middle = int(len(race) / 2)
left_car = race[:middle:]
right_car = list(reversed(race[middle+1::]))


def time(seconds_list):
    res = 0
    for i in seconds_list:
        res += i
        if i == 0:
            res *= 0.8
    return res


left_sum = time(left_car)
right_sum = time(right_car)
if left_sum < right_sum:
    print(f"The winner is left with total time: {left_sum:.1f}")
else:
    print(f"The winner is right with total time: {right_sum:.1f}")



