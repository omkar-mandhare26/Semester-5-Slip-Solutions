def finbonacci_generator():
    a = 0
    b = 1

    while True:
        yield a
        temp = a
        a = b
        b= temp + b

n = 10
fib = finbonacci_generator()
for i in range(n):
    print(next(fib))