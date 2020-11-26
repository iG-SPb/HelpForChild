print("line >>", end="")
num_line = int(input())
print("column >>", end="")
num_column = int(input())
print("victory >>", end="")
num_victory = int(input())

array = [["."] * num_column for i in range(num_line)]

#for row in array:
#    print(' '.join(row))
step = 0

for line in range(num_line - num_victory + 1):  # смещение вниз построчно
    for k in range(num_column - num_victory + 1):  # смещение вправо по столбцам
        for i in range(num_line - line):  # смещение по диагонали
            if k + i == num_column:
                break
            step += 1
            # print("step-", step, line, k, i, (line + i), (k + i))
            array[line + i][k + i] = "S"

            # print("step-", step, line, k, i, (line + i), (num_column - k - i - 1))
            array[line + i][num_column - k - i - 1] = "Y"

for row in array:
    print(' '.join(row))
