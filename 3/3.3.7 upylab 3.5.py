x = int(input())
y = int(input())

if y % x == 0 or x % y == 0:
    print(False)
else:
    print(True)