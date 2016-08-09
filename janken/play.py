HANDS = ['グー', 'チョキ', 'パー']


def select_hand():
    """
    コンピュータの手をランダムに決める
    :return: HANDSの中のいずれか。
    """

    import random
    random.choice(HANDS)
    pass


def judgement(player, computer):
    """
    じゃんけんの勝敗を判定する。
    :param player: HANDSの」中のどれか
    :param computer: HANDSの中のどれか
    :return: プレイヤーが勝ちの場合は1,あいこは0、負けは-1を返す
    """
    if computer == 'グー':
        if player == 1:
            print(0)
        elif player == 2:
            print(-1)
        elif player == 3:
            print(1)
    if computer == 'チョキ':
        if player == 1:
            print(1)
        elif player == 2:
            print(0)
        elif player == 3:
            print(-1)
    if computer == 'パー':
        if player == 1:
            print(-1)
        elif player == 2:
            print(1)
        elif player == 3:
            print(0)

    pass


def save_score(result):
    """
    'score.txt'に戦績を保存
    win:x lose:y draw:zのディクショナリデータを保存する。
    :param result:
    :return: None
    """
    f = open('score.txt', 'w')
    pass


if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)をを選んでください(数字): '))
    computer = select_hand()
    result = judgement(player, computer)
    print(result)
    # コンピュータの手と勝敗の結果を表示
    save_score(result)
