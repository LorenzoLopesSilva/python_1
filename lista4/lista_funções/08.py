def fibonacci(n):
    a = 0
    b = 1

    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
        return b


n = int(input("Digite n: "))
print(fibonacci(n))
