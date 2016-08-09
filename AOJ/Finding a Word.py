W = input().lower()

count = 0
while True:
    line = input()
    if line == 'END_OF_TEXT':
        break

    for s in line.lower.split():
        if s == W:
            count += 1



print(count)