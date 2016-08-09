data = [
    [[0 for r in range(10)] for f in range(3)] for b in range(4)
]

count =int(input())
for c in range(count):
    b, f, r, v = [int(i) for i in input().split()]
    data[b-1][f-1][r-1] += v

for bi, b in enumerate(data):
    for f in b:
        for r in f:
            print(' {0}'.format(r), end='')

        print()
    if bi < 3:
        print('#' * 20)