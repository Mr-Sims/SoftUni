


























################################################################33
####################### РЕШЕНИЕ Инес ##############################

neighbourhood = [int(el) for el in input().split("@")]
line = input()
position = 0

while line != "Love!":
    length = int(line.split()[1])
    position += length
    if position >= len(neighbourhood):
        position = 0
    if neighbourhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighbourhood[position] -= 2
        if neighbourhood[position] == 0:
            print(f"Place {position} has Valentine's day.")

    line = input()
print(f"Cupid's last position was {position}.")
if sum(neighbourhood) == 0:
    print("Mission was successful.")
else:
    count = len([el for el in neighbourhood if el > 0])
    print(f"Cupid has failed {count} places.")