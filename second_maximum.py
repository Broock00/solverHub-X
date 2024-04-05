def sec_max():
    lst = set(arr)
    lst.remove(max(lst))
    return max(lst)
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sec_max())
