'''
授業中にもかかわらず遊んでしまうdaveは、
理科の実験中に、色んな重さの種類があるおもりをすべて使って、
ちょうど天秤が水平になるおもりの組み合わせがあるかを知りたくなったようで、それに遊び呆けてる。
（すべてのおもりを使うため、使わなかったおもりはない。）

あなたは、daveにその組み合わせがあるかどうか教えて、授業に集中させるようにしてください。

もしそのような組み合わせがあれば possiblepossible 、なければ impossibleimpossible を出力してください。
'''


def last_one(l):
    last_index = 0
    for num_i, i in enumerate(l):
        if i == 1:
            last_index = num_i
    return last_index


def match_sum(l, a, where_sum=0):

    for num_i, i in enumerate(l):
        #print(i, a)
        if i < a:
            r_list = match_sum(l[num_i + 1:], a - i, where_sum + num_i + 1)
            if -1 not in r_list:
                return [num_i + where_sum] + r_list
            else:
                continue
        elif i == a:
            return [num_i + where_sum]
    return [-1]

if __name__ == '__main__':

    A = int(input())
    S = list(map(int, input().split()))
    S.sort()
    S.reverse()
    half_sum = sum(S) / 2

    if sum(S) % 2 == 1:
        print("impossible")
    else:
        if -1 in match_sum(S, half_sum):
            print("impossible")
        else:
            print("possible")
