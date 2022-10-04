n = int(input())
s = ""
somme = []

if n == 0:
    print(0)
elif n == -1:
    s = input()
    while s != "F":
        somme.append(s)
        s = input()
    print(sum(eval(i) for i in somme))
else:
    for m in range(0, n):
        s = int(input())
        somme.append(s)
    print(sum(somme))