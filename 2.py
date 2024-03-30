def quick_sort(alist, start, end):
    i = start
    j = end
    arr = alist[(start + end) // 2]
    while True:
        while alist[i] < arr:
            i = i + 1
        while alist[j] > arr:
            j = j - 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
            i = i + 1
            j = j - 1
        else:
            break
    if start < j:
        quick_sort(alist, start, j)
    if i < end:
        quick_sort(alist, i, end)


with open("magical.csv", 'r', encoding="UTF-8") as f:
    a=[x.replace('\n', '').split(',') for x in f.readlines()]

s = []

for i in range(1, len(a)):
    p = 0
    for j in range(len(s)):
        if a[i][0] == s[j][0]:
            p += 1
            if p == 1:
                s[j][1] += int(a[i][1])
                break
    if p == 0:
        s.append([a[i][0], int(a[i][1])])

b = []
for i in range(len(s)):
    b.append([s[i][1], s[i][0]])
quick_sort(b, 0, len(b)-1)
for i in range(5):
    p=str("Зелья ") + str(b[i][1]) + str(" осталось ") +  str(b[i][0])
    print(p)