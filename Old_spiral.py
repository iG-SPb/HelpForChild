# new comment
print("start new >>", end="")
n = int(input())
array = [[".."] * n for i in range(n)]
line = 1
column = 1
step = (4 * n) - 4
position_end_column = 0
position_end_line = 0

for i in range(n):
    array[0][i] = str((i + 1))
    array[n - 1][n - 1 - i] = str((2 * n) - 1 + i)
for i in range(1, (n - 1)):
    array[n - i - 1][0] = str((3 * n) - 2 + i)
    array[i][n - 1] = str((n + i))

while step != n * n:
    i = 0
    while array[line][column + i] == "..":  # шагаем вправо
        step += 1
        array[line][column + i] = str(step)
        i += 1  # шаг вправо
    column = column + i - 1
    line += 1

    i = 0
    while array[line + i][column] == "..":  # шагаем вниз
        step += 1
        array[line + i][column] = str(step)
        i += 1  # шаг вниз
    line = line + i - 1
    column -= 1
    i = 0

    while array[line][column - i] == "..":  # шагаем влево
        step += 1
        array[line][column - i] = str(step)
        i += 1
    line -= 1
    column = column - i + 1

    i = 0
    while array[line - i][column] == "..":  # шагаем вверх
        step += 1
        array[line - i][column] = str(step)
        i += 1
    line = line - i + 1
    column += 1

for row in array:
    print(' '.join(row))