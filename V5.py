
'''
1. INPUTS IN PYTHON:

s=input('Enter String: ')
print(s)

n=int(input("Enter Number: "))
print(n)

f=float(input('Enter Floating point number: '))
print(f)

2. LOOPS IN PYTHON:


A. if-elif-else ladder:
Single if statement has multiple elif statements.

n%5=Buzz
n%3=Fizz
n%3,5=FizzBuzz

n=int(input("Enter Number: "))
if n%3==0 and n%5==0:
    print('FizzBuzz')
elif n%3==0:
    print('Fizz')
elif n%5==0:
    print('Buzz')
else:
    print('Number is not divisible by 3,5')


B. Range Function in Python:

 a. range(10):
 b. range(1,10):
 c. range(0,10,2):
 d. range(10,2,-1):
 
for i in range(10):
    print(i)

for i in range(20,0,-3):
    print(i)

C. for loop in Pyhton:
   
for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Buzz')
    elif i%5==0:
        print('Fizz')
    else:
        print(i, 'is not divisible by 3,5')


'''

for i in range(1,6):
    print(" "*(5-i)+'*'*i+"*"*(i-1))














































