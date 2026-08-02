t = int(input())

for _ in range(t):
    n = int(input())

    per1 = input().split(); pe1 = set(per1)
    per2 = input().split(); pe2 = set(per2)
    per3 = input().split(); pe3 = set(per3)

    po1 = po2 = po3 = 0

    for i in range(n):
        po1 += 0 if per1[i] in pe2 and per1[i] in pe3 else 1 if per1[i] in pe2 or per1[i] in pe3 else 3
        po2 += 0 if per2[i] in pe1 and per2[i] in pe3 else 1 if per2[i] in pe1 or per2[i] in pe3 else 3
        po3 += 0 if per3[i] in pe1 and per3[i] in pe2 else 1 if per3[i] in pe1 or per3[i] in pe2 else 3

    print(po1, po2, po3)
