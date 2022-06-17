import random
import itertools
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

def list_1D_to_2D(l):
    return [l[i:i+3] for i in range(0, 8, 3)]

all_event = [0, 0, 0, 0, 0, 0, 0, 0, 0]

list_set = [7, 1, 2, 3, 4, 5, 6]
r = itertools.product(list_set, repeat=9)
for i in r:
    board = list_1D_to_2D(list(i))
    total_line = check_line(board)
    all_event[total_line] += 1
for idx, val in enumerate(all_event):
    if idx == 7:
        print(f"7條: 你能生出七條除非你老爸變成兔子")
    else:
        print(f"{idx}條: {all_event[idx] * 100 / 7 ** 9:f} %")

print()
print("=========以下為8個門總計結果=========")
total_prob = (7 ** 9) ** 8
all_line = [0, 1, 2, 3, 4, 5, 6, 7, 8]
all_combine = zip(all_line, all_event, )
all_result = {}
r = itertools.product(all_combine, repeat=8)
for i in r:
    #print(i)
    line_sum = 0
    event_sum = 1
    for door in range(len(i)):
        line_sum += i[door][0]
        event_sum *= i[door][1]
    if event_sum == 0:
        continue
    if line_sum not in all_result:
        all_result[line_sum] = event_sum
    else:
        all_result[line_sum] += event_sum
for k in range(65):
    if k == 63:
        print(f'63條線: 如果開出這個選項請打爆老蘇光頭 bbssDj')
    else:
        print(f'{k}條線: {od[k] * 100 / total_prob:.20f}%')
print("====================================")
print(f'3+條線機率: {(total_prob - od[0] - od[1] - od[2]) * 100 / total_prob:.20f}%')
print(f'4+條線機率: {(total_prob - od[0] - od[1] - od[2] - od[3]) * 100 / total_prob:.20f}%')
print(f'5+條線機率: {(total_prob - od[0] - od[1] - od[2] - od[3] * od[4]) * 100 / total_prob:.20f}%')
