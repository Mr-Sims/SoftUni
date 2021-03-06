rows = int(input())
battlefield = []
ships_destroyed = 0

for row in range(0, rows):
    battlefield.append(list(map(int, input().split())))

attacks = input().split()
for attack in attacks:
    row = int(attack.split("-")[0])
    col = int(attack.split("-")[1])

    if battlefield[row][col] == 0:
        continue

    elif battlefield[row][col] == 1:
        battlefield[row][col] = 0
        ships_destroyed += 1

    elif battlefield[row][col] > 1:
        battlefield[row][col] -= 1

print(ships_destroyed)