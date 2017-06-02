A, B, C = map(int, input().split())
S = list(map(int, input().split()))

sum_all = 0
for x in S:
    sum_all += x

amari = A * B - sum_all
if amari >= 0:
    print(amari)
else:
    print(-1)
