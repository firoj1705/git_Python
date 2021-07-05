'''
While Loop: For unknown itrations.

a.

c=0
while True:
   if c<7:
       print("Hello")
       c=c+1

b.
while True:
    s=input("Enter String: ")
    if s=='abcd':
        print("Password is correct")
        break
    else:
        print("Please enter correct password")

c. WAP to write average of 'n' nos.
total=0
count=0
while True:
    num=input("Enter number or `stop` to break: ")
    if num=='stop':
        break
    else:
        total=total+float(num)
        count=count+1
avg=total/count
print("Average is", avg)

d. WAP for infinite loop:

s=input("Enter Number: ")
while len(s)<5:
    print(s)

e. WAP for finite loop:

while True:
    s=input("Enter String: ")
    if len(s)<5:
        print('hi')
    else:
        break


FUNCTIONS IN PYTHON:

1. Built in functions: we cannot write it. 
2. User Defined functions
3. Recursive functions
4. Anonymous functions(Lambda funcions)


User Defined functions:
a. Parameterized function:(in this function, values are given in brackets.)

def add(a,b):    # def is keyword
    print("Addition is: ", a+b)    # print is function
add(3,5)


def add(a,b):
    print("Addition is: ", a+b)
add(int(input("Enter a: ")), int(input("Enter b: ")))


def multiply(a,b):
    print("Multiplication is: ",a*b)
multiply(5,7)


def divide(a,b):
    print("Dividation is: ", a/b)
divide(56,7)


def power(a,b):
    print("Power is: ",a**b)
power(4,5)


'''


























