#WAP to find the factorial of n using non-recursive and recursive function methods
#Input : n=5
#Output : 120


def factorial(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    
    return res


def factorial_recursive(n):
    if n<=1:
        return 1
    
    return n * factorial(n-1)


n = int(input())
print(factorial(n))
print(factorial_recursive(n))