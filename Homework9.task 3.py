def find_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n / i))
    divisors.sort()
    return(divisors)
n = int(input())
print(find_divisors(n))