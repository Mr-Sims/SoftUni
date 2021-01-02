# Напишете програма, която ви помага при товаренето на куфари в багажника на самолет.
# Всеки самолет има определен капацитет на багажника.
# До получаване на команда "End" ще получавате обем на куфар.
# Обемът на всеки трети куфар трябва да се увеличава с 10%, поради загубата на пространство при начина на подреждане.
# Ако свободното пространството в даден момент е по-малко от обема на куфар товаренето трябва да прекъсне.

# Вход
# Първоначално се чете един ред:
# •	Капацитетът на багажника – реално число в диапазона [100.0…6000.0]
# След това до получаване на команда "End" или до запълване на багажника, се чете по един ред:
# o	Обем на куфар – реално число в диапазона [100.0…6000.0]
trunk_capacity = float(input())
fullness = 0
line = input()
count = 0
while line != "End":
    suitcase_size = float(line)
    count += 1
    if count % 3 == 0:
        suitcase_size *= 1.1
    fullness += suitcase_size
    if fullness > trunk_capacity:
        print("No more space!")
        count -= 1
        break
    line = input()
if fullness <= trunk_capacity:
    print(f"Congratulations! All suitcases are loaded!")
print(f"Statistic: {count} suitcases loaded.")

# Изход
# На конзолата да се отпечатат следните редове според случая:
# •	При получаване на командата "End" се печата:
# "Congratulations! All suitcases are loaded!"
# •	Ако обемът на куфара е по-голям от оставащото пространство в багажника:
# "No more space!"
# •	Накрая винаги се отпечатва статистика – колко багажа са натоварени:
# "Statistic: {брой натоварени багажи} suitcases loaded."
