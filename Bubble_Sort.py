def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                count += 1
    print("Array is sorted in %s swaps." % count)
    print("First Element: %s" % a[0])
    print("Last Element: %s" % a[-1])
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
