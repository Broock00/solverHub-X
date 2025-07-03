n = input().split()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
j = 0
c = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
c += a[i:]
c += b[j:]

result = ' '.join(map(str, c))
print(result)
