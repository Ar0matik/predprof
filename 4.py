def class_potion(a):
    return a[a.find(" "):]

def name_potion(a):
    return a[:a.find(" ")]

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
    p = 0
    for j in range(len(b)):
        if class_potion(s[i][0]) == b[j][0]:
            p += 1
            if p == 1:
                b[j][1] += int(a[i][1])
                b[j][2] += 1
                break
    if p == 0:
        b.append([class_potion(s[i][0]), int(s[i][1]), 1])
for i in range(len(b)):
    p=str(b[i][2]) + str(" зелий класса ") + str(b[i][0]) + str(",  общее количество зелий ") + str(b[i][1])
    print(p)