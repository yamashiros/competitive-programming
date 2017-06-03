'''
ここに0番〜(N-1)番の品物がある。
また、
item1 item2 score
という形式で書かれた得点表がある。
品物を並べた時、item1がitem2よりも前であればscore点を獲得できるという意味である。

得点表が与えられるので、品物を適切に並び替えた時、獲得できる得点を最大化したい。そのときの得点を出力せよ。

注意：LL系の言語だと工夫しないといけないかもしれません。
'''
import itertools
N, M = map(int, input().split())
n_list = list(itertools.permutations(range(N)))
m_list = []
for i in range(M):
    m_list.append(list(map(int, input().split())))

score_max = 0
for i in n_list:
    score_now = 0
    for j in m_list:
        if list(i).index(j[0]) < list(i).index(j[1]):
            score_now += j[2]
    if score_now > score_max:
        score_max = score_now
print(score_max)
