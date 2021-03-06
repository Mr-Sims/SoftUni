# Преди време Петър си е купил биткойн. Сега ще ходи на екскурзия из Европа и ще му трябва евро. Освен биткойн има и китайски юанa. Той иска да обмени парите си в евро за екскурзията. Напишете програма, която да пресмята колко евро може да купи спрямо следните валутни курсове:

# •	1 биткойн = 1168 лева.
# •	1 китайски юан = 0.15 долара.
# •	1 долар = 1.76 лева.
# •	1 евро = 1.95 лева.
# Обменното бюро има комисионна от 0 до 5 процента от крайната сума в евро.

# Изход
# На конзолата да се отпечата 1 число - резултатът от обмяната на валутите.
# Резултатът да се форматира до втория знак след десетичната запетая.
## Вход
# От конзолата се четат 3 числа:
bitcoin_count = int(input())         # броят биткойни. Цяло число в интервала [0…20]
yunan_count = float(input())           # броят китайски юана. Реално число в интервала [0.00… 50 000.00]
commission = float(input())           #  комисионната. Реално число в интервала [0.00 ... 5.00]

bitcoin = 1168
dollar = 1.76
euro = 1.95
yuan = 0.264

total_bitcoin = bitcoin_count * bitcoin
total_yuan = yunan_count * yuan
total_euro = ((total_yuan + total_bitcoin) / euro) - ((total_yuan + total_bitcoin) / euro) * (commission / 100)
print(f"{total_euro:.2f}")