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

for i in range(len(s)):
    if s[i][0] == 'Мощное Зелье':
        print("Данного зелья осталось -", s[i][1])

with open('magicalPotions.txt','w', encoding='UTF-8' ) as f:
    for i in range(len(s)):
        p = s[i][0] + str(" в запасах еще есть - ") + str(s[i][1])
        f.write("%s\n" % p)

