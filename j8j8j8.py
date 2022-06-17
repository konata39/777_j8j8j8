import random

def check_line(a):
    line = 0
    for i in range(3):
        if a[0][i] == a[1][i] and a[0][i] == a[2][i] and a[1][i] == a[2][i]:
            line += 1
        if a[i][0] == a[i][1] and a[i][0] == a[i][2] and a[i][1] == a[i][2]:
            line += 1
    if a[0][0] == a[1][1] and a[2][2] == a[1][1] and a[0][0] == a[2][2]:
        line += 1
    if a[0][2] == a[1][1] and a[2][0] == a[1][1] and a[0][2] == a[2][0]:
        line += 1
    return line

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
eight = 0

list_set = [7, 1, 2, 3, 4, 5, 6]
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for _1 in list_set:
    board[0][0] = _1
    for _2 in list_set:
        board[0][1] = _2
        for _3 in list_set:
            board[0][2] = _3
            for _4 in list_set:
                board[1][0] = _4
                for _5 in list_set:
                    board[1][1] = _5
                    for _6 in list_set:
                        board[1][2] = _6
                        for _7 in list_set:
                            board[2][0] = _7
                            for _8 in list_set:
                                board[2][1] = _8
                                for _9 in list_set:
                                    board[2][2] = _9
                                    total_line = check_line(board)
                                    if total_line == 0:
                                        zero += 1
                                    elif total_line == 1:
                                        one += 1
                                    elif total_line == 2:
                                        two += 1
                                    elif total_line == 3:
                                        three += 1
                                    elif total_line == 4:
                                        four += 1
                                    elif total_line == 5:
                                        five += 1
                                    elif total_line == 6:
                                        six += 1
                                    elif total_line == 8:
                                        eight += 1
print("0條: ", zero / 7 ** 9)
print("1條: ", one / 7 ** 9)
print(two / 7 ** 9)
print(three / 7 ** 9)
print(four / 7 ** 9)
print(five / 7 ** 9)
print(six / 7 ** 9)
print(eight / 7 ** 9)
