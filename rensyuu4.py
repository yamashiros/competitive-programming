
N, M = map(int, input().split())
score_list = [-float("inf")] * (N + 1)
score_list[1] = 0
m_list = []
for i in range(M):
    m_list.append(list(map(int, input().split())))

m_list.sort(key=lambda x: x[0])
score_keep = 0
for count in [0, 1]:
    for x in m_list:
        if score_list[x[0]] + x[2] > score_list[x[1]]:
            score_list[x[1]] = score_list[x[0]] + x[2]
    if count == 0:
        score_keep = score_list[N]

if score_keep == score_list[N]:
    print(int(score_list[N]))
else:
    print("inf")
