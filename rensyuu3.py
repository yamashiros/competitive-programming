N, K = map(int, input().split())
count = 0
m_list = []
for i in range(N):
    m_list.append(list(map(int, input().split())))

m_list.sort(key=lambda x: x[0])

for m in m_list:
    count += m[1]
    if count >= K:
        print(m[0])
        break
