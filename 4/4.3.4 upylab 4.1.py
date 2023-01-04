def deux_egaux(a, b, c):
    if a == b or a == c or b == c:
        return True
    else:
        return False


x = int(input())
y = int(input())
z = int(input())

print(deux_egaux(x, y, z))
