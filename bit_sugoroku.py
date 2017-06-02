'''
Carol は特殊なすごろくをしようとしている。

1からNの番号がふられている一直線に並べられているN個のマスがある。
1から開始のマスとして、ゴールはNが書かれているマスとする。

その場に書かれている数字の2進数で表現した時の1のビット数 だけ「前」または「後」に進めることができる。
(1未満とN+1以上のマスには移動することは出来ない、正確にNにならないとゴールできない）

自然数Nを与えられた時、ゴールに到達できる最短の移動数（開始のマスへも移動にカウントする）を求めてください。
到達できない場合は-1を出力してください。

開始のマスがすでにゴールになっている場合もあリます。
'''
MAX_STEP = 100000


def my_bin(x):
    return bin(x).count("1")

if __name__ == '__main__':
    A = int(input())
    bit_one_list = list(map(my_bin, range(1, A + 1)))
    din_list = [MAX_STEP] * A
    din_list[0] = 0
    now_step = 0
    hohaba = 0
    step_count = 0
    step_queue = [now_step]
    while len(step_queue) > 0:
        now_step = step_queue.pop(0)
        hohaba = bit_one_list[now_step]
        step_count = din_list[now_step]
        if now_step + hohaba + 1 <= A and step_count + 1 < din_list[now_step + hohaba]:
            step_queue.append(now_step + hohaba)
            din_list[now_step + hohaba] = step_count + 1
        if now_step - hohaba + 1 > 0 and step_count + 1 < din_list[now_step - hohaba]:
            step_queue.append(now_step - hohaba)
            din_list[now_step - hohaba] = step_count + 1
    if din_list[A - 1] != MAX_STEP:
        print(din_list[A - 1] + 1)
    else:
        print(-1)
