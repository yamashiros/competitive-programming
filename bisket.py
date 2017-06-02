A = int(input())
num_b = 1
count = 0
# num_b_dec = num_b

# while A != num_b:
#     if num_b_dec * 2 <= A:
#         num_b += num_b_dec
#         num_b_dec = num_b
#         count += 1
#     else:
#         num_b_dec -= 1

while num_b < A:
    num_b *= 2
    count += 1
print(count)
