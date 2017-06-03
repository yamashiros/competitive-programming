N, Q = map(int, input().split())
a_list = [chr(i) for i in range(65, 65 + N)]


def devider(list_n):
    list_r = []
    list_l = []
    if len(list_n) > 1:
        for x in list_n[1:]:
            print("? " + list_n[0] + " " + x)
            S = str(input())
            if S == ">":
                list_l.append(x)
            elif S == "<":
                list_r.append(x)
        return devider(list_l) + [list_n[0]] + devider(list_r)
    else:
        return list_n

if __name__ == '__main__':
    print("! " + "".join(devider(a_list)))
