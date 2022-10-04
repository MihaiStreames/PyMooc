def fibo(n):
    if n < 2:
        res = n
    else:
        res = fibo(n-1) + fibo(n-2)
    return res

for i in range(10):
    print(fibo(i))