'''
あなたと素数を習ったばかりのEveは、素数のゲームを思いついた。

ゲームの内容は以下のとおりです。
・まず初めに、先攻のプレイヤーに22以上の自然数NNが与えられます。
・その番のプレイヤーはNNに対して、「NN以下（NNも含む）の素数」のどれかで減算する、
その数をN′N′とすると、N′N′が00または11になってしまったら、そのプレイヤーの負けである。
・その後N′N′を新たなNNとし、相手にその数を渡し、以上を繰り返します。

まずあなたが先攻となりゲームを始めます。
この時、どちらも負けないように動くと考える。自然数NNが与えられた時、
あなたが勝つことが出来る場合WinWin、それ以外はLoseLoseを返してください。
'''


def prime_maker(x):
    prime_list = [True] * (x + 1)
    for i in range(2, x + 1):
        if prime_list[i]:
            for j in range(i + 1, x + 1):
                if j % i == 0:
                    prime_list[j] = False
    prime_list1 = []
    for y_num, y in enumerate(prime_list):
        if y:
            prime_list1.append(y_num)

    return prime_list1[2:]


if __name__ == '__main__':

    A = int(input())
    prime_list = prime_maker(A)
    score_list = [False] * (A + 1)
    score_list[0] = True
    score_list[1] = True
    count = 0
    for i in range(2, A + 1):
        for j in prime_list:
            if i >= j and not score_list[i - j]:
                score_list[i] = True
    if score_list[A]:
        print("Win")
    else:
        print("Lose")
