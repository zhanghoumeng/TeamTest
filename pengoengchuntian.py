

L = [11,12,3,13,19,45,23,14]


def Sort_1(L):
    for i in range(len(L)-1):
        for j in range (i, len(L)-1):
            if L[i] > L[j+1]:
                L[i],L[j + 1] = L[j + 1], L[i]
    return L
a = Sort_1(L)
print(a)