while True:
    try:
        x = int(input("数字を入れてください: "))
        break
    except (ValueError, NameError, TypeError):
        print("あらら！これは有効な数字ではありません。どうぞもう一度...")
