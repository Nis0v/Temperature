ls = []
ls1 = []
lst = {}
n = int(input())
while n != 0:
    n -= 1
    ls.append(input().replace(":", " ").split())
for n in ls:
    if len(n) == 1:
        lst[n[0]] = []
    elif len(n) > 1:
        k1 = n[0]
        lst[k1] = n
for key, values in lst.items():
    for value in values:
        if value == key:
            values.remove(value)
for k, v in lst.items():
    for k2, v2 in lst.items():
        if k in v2:
            for i in v:
                if v[0] not in lst[k2]:
                    lst[k2] += v
print(lst)
n = int(input())
while n != 0:
    n -= 1
    ls1.append(input().split())
for n in ls1:
    if len(n) > 1:
        if n[0] == n[1]:
            print("Yes")
        elif n[1] in lst.keys():
            if n[0] in lst[n[1]]:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
