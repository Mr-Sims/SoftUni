line = input()
line_as_list = line.split(", ")

for i in range(len(line_as_list)-1, -1, -1):
    if line_as_list[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif line_as_list[i] == "wolf":
        print(f"Oi! Sheep number {len(line_as_list)-1 - i}! You are about to be eaten by a wolf!")