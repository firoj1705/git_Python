'''
Recursive Functions:
1. WARP to write factorial of number:

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(10))
print(factorial(5))

2. WARP to find fibonacci number:

def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-2)+fib(n-1)
print(fib(5))
print(fib(10))


for i in range(int(input("How many fib no. you want?: "))):
    print(fib(i), end=", ")


3. WARP to find sum of digits in given number:

'''

def sum_digit(n):
    if n==0:
        return 0
    else:
        return (n%10)+sum_digit(n//10)
print(sum_digit(int(input("Sum of digits of for number is: "))))
print(sum_digit(1995))


































