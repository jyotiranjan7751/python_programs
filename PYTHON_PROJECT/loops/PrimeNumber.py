def isPrime(n):
    for i in range(2, int(n / 2)):
        if n % i == 0:
            return False 
    return True


for i in range (1, 100):
    res = isPrime(i)
    if res:
        print(i)
