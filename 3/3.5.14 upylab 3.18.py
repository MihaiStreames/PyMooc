hauteur = int(input())

def foo(n):
  return "".join([str((i+n)%10) for i in range(1, n+2)] + [str((i+n)%10) for i in range(1, n+1)][::-1])

final = ""
lenS = 1
for i in range(hauteur):

  a = foo(i)

  s = " "*(hauteur-1) + a
  lenS += 2
  final += s + "\n"
  hauteur -= 1

print(final[:-1])