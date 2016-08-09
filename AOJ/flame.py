while True:
    H, W = [int(i) for i in input().split()]
    if H == W == 0:
        break

    for h in range(H):
        for w in range(W):
            if h == 0 or h == H -1 or w == 0 or w == W -1:
                print('#', end='')
            else:
                print('.', end='')

        print()

    print()
