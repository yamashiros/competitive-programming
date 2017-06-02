L = list(map(int, input().split()))

x = int(L[1] / L[0])
if L[1] - x * L[0] > 0:
    x += 1
print(x)
