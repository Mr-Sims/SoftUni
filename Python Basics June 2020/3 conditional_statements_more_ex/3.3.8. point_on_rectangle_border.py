# Напишете програма, която проверява дали точка {x, y} се намира върху някоя от страните
# на правоъгълник {x1, y1} – {x2, y2}.
# Да се отпечата "Border" (точката лежи на някоя от страните) или "Inside / Outside" (в противен случай).
# * Подсказка:
# използвайте една или няколко условни if проверки с логически операции.
# Точка {x, y} лежи върху някоя от страните на правоъгълник {x1, y1} – {x2, y2},
# ако е изпълнено едно от следните условия:
# •	x съвпада с x1 или x2 и същевременно y е между y1 и y2
# •	y съвпада с y1 или y2 и същевременно x е между x1 и x2
# Можете да проверите горните условия с една по-сложна if-else конструкция или с няколко по-прости проверки или с вложени if-else проверки

# Вход - като се гарантира, че x1 < x2 и y1 < y2).
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if (x == x1 or x == x2) and (y >= y1 and y <= y2) or (y == y1 or y == y2) and (x >= x1 and x <= x2):
    print("Border")
else:
    print("Inside / Outside")