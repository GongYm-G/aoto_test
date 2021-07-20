def zf1(i, n):
    num = range(n)
    number = 0
    # i = 19995
    start = 0
    stop = len(num)
    index = stop // 2
    while True:
        if i < num[index]:
            stop = index
            index = (index - start - 1) // 2 + start
        elif i > num[index]:
            start = index
            index = (stop - index + 1) // 2 + index
        else:
            print(index)
            break
        number += 1
        print("%d - %d" % (start, stop))
    print(number)


def zf2(i, n):
    num = range(n)
    number = 0
    # i = 19995
    start = 0
    stop = len(num)
    index = stop // 2
    while True:
        if i < num[index]:
            stop = index
            index = (index - start) // 2 + start
        elif i > num[index]:
            start = index
            index = (stop - index) // 2 + index
        else:
            print(index)
            break
        number += 1
        print("%d - %d" % (start, stop))
    print(number)


def zf3(i, n):
    num = range(n)
    start = 0
    stop = len(num)
    index = stop // 2
    while True:
        if i < num[index]:
            stop = index
            index = (index - start) // 2 + start
        elif i > num[index]:
            start = index
            index = (stop - index) // 2 + index
        else:
            break


# i = 9009
# n = 10001
# zf1(i, n)
# zf2(i, n)
