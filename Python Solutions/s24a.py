n = 7

isPrime = True
for i in range(2, n):
    if n % i == 0: isPrime = False

factorial = 1
for i in range(1, n+1):
    factorial *= i

print(f"Is {n} prime? {isPrime}")
print(f"Factorial of {n} = {factorial}")