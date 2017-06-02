N = int(input())
S = str()
for i in range(1, N + 1):

    if i % 3 == 0:
        S += "Fizz"
    if i % 5 == 0:
        S += "Buzz"
    if i % 3 != 0 and i % 5 != 0:
        S += str(i)
    S += ("\n")
print(S)
