#数字を文字列として扱う場合
while True:
    data = input()
    if data == '0':
        break

    print(sum([int(i) for i in data]))
"""
while True:
    data = int(input())
    if data == 0:
        break

    for i in range():
"""