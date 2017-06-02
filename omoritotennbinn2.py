'''
授業中にもかかわらず遊んでしまうdaveは、
理科の実験中に、色んな重さの種類があるおもりをすべて使って、
ちょうど天秤が水平になるおもりの組み合わせがあるかを知りたくなったようで、それに遊び呆けてる。
（すべてのおもりを使うため、使わなかったおもりはない。）

あなたは、daveにその組み合わせがあるかどうか教えて、授業に集中させるようにしてください。

もしそのような組み合わせがあれば possiblepossible 、なければ impossibleimpossible を出力してください。
'''

if __name__ == '__main__':

    A = int(input())
    S = list(map(int, input().split()))

    half_sum = sum(S) / 2

    if sum(S) % 2 == 1:
        print("impossible")
    else:
        half_sum = int(half_sum)
        r_list = [False] * (half_sum + 1)
        r_list[0] = True
        for i in S:
            for j in range(half_sum, -1, -1):
                if r_list[j] and j + i <= half_sum:
                    r_list[j + i] = True
        if r_list[half_sum]:
            print("possible")
        else:
            print("impossible")
