'''
1. Write a Python program to sum all the items in a list

L=[1,2,3,4,5,6]

c=0
for i in L:
    c=c+i
print(c)

2. Write a Python program to multiplies all the items in a list. 

L=[1,2,3,4,5,6]

c=1
for i in L:
    c=c*i
print(c)                   #My solution


def multiply_items(L):
    c=1
    for i in L:
        c=c*i
    return c
print(multiply_items([1,2,3,4,5,6]))

3. Write a Python program to get the largest number from a list.

def largest_no(list):
    c=0
    for i in list:
        if i>c:
            c=i
    return c
print(largest_no([1,2,3,4,5,6]))


t=[1,2,3,4,5,6]
c=0
for i in t:
    if i>c:
        c=i
print("Largest no from List is: ",c)


4. Write a Python program to get the smallest number from a list.

L=[1,2,3,4,5,6,-1,0,-2,-10]

c=0
for i in L:
    if i<c:
        c=i
print("Min number in list is : ", c)


5. Write a Python program to count the number of strings where the string length is 2 or more
and the first and last character are same from a given list of strings.

L= ['abc', 'xyz', 'aba', '1221']

L1=[]

for i in L:
    if i[0]==i[-1]:
        L1.append(i)
print("List is: ", L1 , "and Number of such characters are: ", len(L1))     #List is:  ['aba', '1221'] and Number of such characters are:  2

ALSO

L= ['abc', 'xyz', 'aba', '1221', 'ab', 'aa']

L1=[]

for i in L:
    if i[0]==i[-1] and len(i)>=3:
        L1.append(i)
print("List is: ", L1 , "and Number of such characters are: ", len(L1))     #List is:  ['aba', '1221'] and Number of such characters are:  2


6. Write a Python program to get a list, sorted in increasing order by the last element
in each tuple from a given list of non-empty tuples.

L=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

##L.sort()
##print(L)    #[(1, 2), (2, 1), (2, 3), (2, 5), (4, 4)]
##
###but we want increasing order by the last element

L1=[]
for i in range(len(L)):
    L1.append(L[i][::-1])                        #if we use range(len(L)) then we can use L[i]
print(L1)

L1.sort()
print(L1)

L2=[]
for i in range(len(L1)):
    L2.append(L1[i][::-1])                       
print(L2)


7. Write a Python program to remove duplicates from a list.


'''
L=[1,2,3,4,1,3,5,7,9]
L1=[]

for i in L:
    if i not in L:
        L1.append(L)
print(L1)
        























    

