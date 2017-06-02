# 標準入力から一行分を読み出し、文字列として格納する。
# first = input()

# # 読み込んだ文字列をスペースで分割する
# split_first = first.split()

# # それぞれをint型に変換する
# A = int(split_first[0])
# B = int(split_first[1])

# 慣れてくると この一行でよい
A, B = map(int, input().split())

# 参考: リストを読む際はlist()で覆ってやらないといけない
# L = list(map(int, input().split()))

# 2行目を読み込む
S = input()

# 標準出力に書き出す。
# カンマで区切るとスペースで分割してくれるので楽です。
print(A + B, S)
