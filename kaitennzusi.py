'''
あなたは、回転寿司にきている。
お寿司はN皿が順番に流れてくる。N皿のお寿司のそれぞれの美味しさがViViで表される。

流れてくるお寿司が自分の前に来た時に取ることができるが、このお店のルールで、
連続で皿を取ることが出来ない。
もちろん、自分の前を過ぎたお寿司も取ることが出来ない。

この時、あなたが得られる美味しさの最大の合計値を求めてください。
お寿司は一周回ってくることはないとする。
'''
A = int(input())
S = list(map(int, input().split()))

score_list = [0] * A
if A > 0:
    score_list[0] = S[0]
if A > 1:
    score_list[1] = S[1]

for i in range(2, A):
    score_list[i] = max(score_list[:i - 1]) + S[i]
print(max(score_list))
