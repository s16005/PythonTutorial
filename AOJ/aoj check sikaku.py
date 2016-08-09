while True:
    H, W = [int(i) for i in input().split()]
    if H == W == 0:
        break

    for h in range(H):
        for w in range(W):
            if (w + h) % 2 == 0  :
                print('#', end='')
            else:
                print('.', end='')

        print()

    print()
