count_symbol1 = 0
count_symbol2 = 0

num_strok = 4
num_stolbets = 6
count_pobeda = 3
symbol = "X"

array_game = [["."] * num_stolbets for i in range(num_strok)]

for line in range(num_strok - count_pobeda + 1):
    for k in range(num_stolbets - count_pobeda + 1):
        count_symbol1 = 0
        count_symbol2 = 0
        for i in range(num_strok - line):
            if i + k == num_stolbets:
                break
            else:
                if array_game[line + i][i + k] == symbol:
                    count_symbol1 += 1
                    if count_symbol1 == count_pobeda:
                        print("victory")
                else:
                    count_symbol1 = 0
                if array_game[line + i][num_stolbets - i - k - 1] == symbol:
                    count_symbol2 += 1
                    if count_symbol2 == count_pobeda:
                        print("victory")
                else:
                    count_symbol2 = 0
print("no victory")