a=[5,3,2,8,4,5,2,5,1,9,5,3]
def distinct(a):
    global res
    res = []
    [res.append(x) for x in a if x not in res]
    return res
distinct_num=sorted(distinct(a))
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
c=distinct_num
new=Repeat(a)
result =c+sorted(new)
print(result)


