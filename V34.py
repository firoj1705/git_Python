'''
EOP Continue......


2. LIST COMPREHENSION:
It is consize way to declare a list where each element in a list is a result of some expression.

Few Examples:

a. WAP to append square of even number in a list for a range(1,21).

L=[]
for i in range(1,21):
    if i%2==0:
        L.append(i*i)
print(L)


L1=[i*i for i in range (1,21) if i%2==0]
print(L1)


b. WAP to check odd and even no.

L=[]
for i in range(1,21):
    if i%2==0:
        L.append(f"{i} is even")
    else:
        L.append(f"{i} is odd")
print(L)

#OR
L1=[f"{i} is even" if i%2==0 else f"{i} is odd" for i in range(1,21)]
print(L1)

#OR
print([f"{i} is even" if i%2==0 else f"{i} is odd" for i in range(1,21)])


c. WAP for if-elif-else:

L=[]

for i in range(1,51):
    if i%3==0 and i%5==0:
        L.append("FizzBuzz")
    elif i%3==0:
        L.append('Buzz')
    elif i%5==0:
        L.append("Fizz")
    else:
        L.append(i)
print(L)


L1=['FizzBuzz' if i%3==0 and i%5==0 else 'Buzz' if i%3==0 else "Fizz" if i%5==0 else i for i in range (1,51)]
print(L1)


d. WAP for 2-D list.

L=[]
for i in range(3):
    L1=[]
    for j in range(3):
        if i==j:
            L1.append(1)
        else:
            L1.append(0)
    L.append(L1)
print(L)

OR
L2=[[1 if i==j else 0 for j in range(3)] for i in range(3)]
print(L2)

'''


            
























