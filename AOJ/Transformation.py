s = input()
q = int(input())

for qi in range(q):
    command = input().split()
    a = int(command[1])
    b = int(command[2])
    if command[0] == 'print':

        print(s[a:b + 1])
    elif command[0] == 'reverse':
        s = s[:a] + s[b::-1] + s[b + 1:]
    else:
        p = command[3]
        s =
