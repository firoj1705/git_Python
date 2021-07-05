'''
DYNAMIC PROGRAMMING: WHEN USER GIVE INPUT IS CALEED DYNAMIC PROGRAMMING.

1. DIAMOND SHAPE

for i in range(1,6):
    print(" "*(5-i)+i*'*'+"*"*(i-1))
for j in range(4,0,-1):
    print(" "*(5-j)+'*'*j+'*'*(j-1))

DIAMOND SHAPE AS PER USER INPUT:

n=int(input("Enter Number: "))
for i in range(1,n+1):
    print(" "*(n-i)+i*'*'+"*"*(i-1))
for j in range(n-1,0,-1):
    print(" "*(n-j)+'*'*j+'*'*(j-1))



2. SQUARE SHAPE:

    A. SQUARE:
        for i in range(1,6):
            print("*"*5)

    As per User input:
        n=int(input("Enter Number: "))
        for i in range(1, n+1):
            print("*"*n)

    B. HOLLOW SQUARE:

        for i in range(1,6):
            if i==1 or i==5:
                print("*"*5)
            else:
                print('*'+" "*3+'*')

    As per user input:
    
        n=int(input("Enter Number: "))
        for i in range(1,n+1):
            if i==1 or i==n:
                print("*"*n)
            else:
                print("*"+" "*(n-2)+"*")


    C. ALPHABETS:
        A-Alphabet:

        for i in range(1,6):
            if i==1:
                print(" "+'*'*3)
            elif i==3:
                print('*'*5)
            else:
                print("*"+" "*3+"*")
 As per user input:
  
n=int(input("Enter number: "))
for i in range(1,n+1):
    if n//2==0:
        if i==1:
            print(' '+'*'*(n-2)+' ')
        elif i==(n//2):
            print('*'*n)
        else:
            print('*'+" "*(n-2)+'*')
    else:
        if i==1:
            print(' '+'*'*(n-2)+' ')
        elif i==((n//2)+1):
            print('*'*n)
        else:
            print('*'+" "*(n-2)+'*')


B-Aplhtabet:

for i in range(1,6):
    if i==1 or i==3 or i==5:
        print("*"*4)
    else:
        print("*"+" "*3+"*")


As per user input:
n=int(input("enter Number: "))
for i in range(1,n+1):
    if n%2==0:
        if i==1 or i==n/2 or i==n:
            print("*"*(n-1))
        else:
            print("*"+(n-2)*" "+"*")
    else:
        if i==1 or i==(n//2)+1 or i==n:
            print("*"*(n-1))
        else:
            print("*"+(n-2)*" "+"*")

'''




        











       



























