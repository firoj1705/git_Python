'''
Problems on List:

1. WAP to insert squares of no.s of the range(1,21) into list.

L=[]
for i in range(1,21):
    L.append(i*i)
print(L)

2. WAP to find maximum no. from list.

L=[1,2,3,4,55,34,36,78,-1]
c=0
for i in L:
    if i>c:
        c=i
print("Maximum no. in list is: ",c)

3. WAP to find minimum no. from list.
L=[1,2,3,4,55,34,36,78,-1]
c=0
for i in L:
    if i<c:
        c=i
print("Minimum no. in list is: ", c)

4. WAP to find sum of no.s from given list.

L=[1,2,3,4,55,34,36,78,-1]
c=0

for i in L:
    c=c+i
print("Sum of no.s is: ",c)

5. WAP to find sum of no.s from list if element is no., if element is string then concat those elements.

L=[1,2,3,4,55,34,10.5,36,78,-1, 'Hi', '10', 'Hello']

c=0
s=' '

for i in L:
    if type(i)==int or type(i)==float:
        c=c+i
    else:
        s=s+i
print("Sum of Nos. is: ", c)
print("String is: ",s)

6. WAP to combine elements of two list if they are not equal.

L1=[1,2,3,4,55,34]
L2=[1,2,5,8,9,36]
L=[]

for i in L1:
    for j in L2:
        if i!=j:
            L.append([i,j])
print(L)     #[[1, 2], [1, 5], [1, 8], [1, 9], [1, 36], [2, 1], [2, 5], [2, 8], [2, 9], [2, 36], [3, 1],
[3, 2], [3, 5], [3, 8], [3, 9], [3, 36], [4, 1], [4, 2], [4, 5], [4, 8], [4, 9],
[4, 36], [55, 1], [55, 2], [55, 5], [55, 8], [55, 9], [55, 36], [34, 1], [34, 2], [34, 5], [34, 8], [34, 9], [34, 36]]

7. WAP to create identity matrix using list of the dimension 3*3.

p=[]
for i in range(3):
    L=[]
    for j in range(3):
        if i==j:
            L.append(1)
        else:
            L.append(0)
    p.append(L)
print(p)


8. WAP to create 2D list where each element of the list is a result of row*col.

L=[]
row = int(input("Enter no. of rows: "))
col = int(input("Enter no. of col: "))

for i in range(row):
        for j in range(col):
            L.append(i*j)
print(L)

TO GET SEPARATE:

L=[]
row = int(input("Enter no. of rows: "))
col = int(input("Enter no. of col: "))

for i in range(row):
    L1=[]
    for j in range(col):
        L1.append(i*j)
        L.append(L1)
print(L)

9. WAP to create 3-D matrix using list.
L=[]
row = int(input("Enter no. of rows: "))
col = int(input("Enter no. of col: "))
depth=int(input("Enter no. of depth: "))

for i in range(row):                               
    L1=[]
    for j in range(col):
        L2=[]
        for k in range(depth):
            L2.append(k*j)
        L1.append(L2)
    L.append(L1)
print(L)     #[[[0, 0, 0], [0, 1, 2], [0, 2, 4]], [[0, 0, 0], [0, 1, 2], [0, 2, 4]], [[0, 0, 0], [0, 1, 2], [0, 2, 4]]]
'''


L=[1,2,3,4,5,6,7,8,9,10,11,12,13]
p=[]

for i in range(len(L)):
    p.append(L[i:i+2])
print(p)






















