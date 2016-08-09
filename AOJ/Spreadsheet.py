r, c = [int(i) for i in input().split()]

data = []
sum_row = [0] * (c + 1)

for ri in range(r):
    data.append([int(i) for i in input().split()])
    data[ri].append(sum(data[ri]))
    print(" ".join([str(d) for d in data[ri]]))
    for ci in range(c + 1):
        sum_row[ci] += data[ri][ci]

print(" ".join([str(s) for s in sum_row]))