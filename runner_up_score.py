def runner_up_score():
    lst = set(arr)
    lst.remove(max(lst))
    return max(lst)
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(runner_up_score())
