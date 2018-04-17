

L = [11,12,3,13,19,45,23,14]


def maopao (list)
    for out in range(len(list)-1,0,-1)
        for inner in range(0,out)
            if list[inner] > list[inner + 1]
            temp = list[inner]
            list[inner + 1] = list[inner]
            list[inner] = temp
        print(list)
