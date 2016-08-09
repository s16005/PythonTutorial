n = int(input())

taro = 0
hanako = 0
for ni in range(n):
    t, h = input().split()

    if t < h :
        hanako += 3
    elif t > h:
        taro += 3
    else:
        hanako += 1
        taro += 1

print(taro, hanako)