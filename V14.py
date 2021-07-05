'''
1. WAP to sort as per last elemnt of tuple.
L=[(1,2),(2,1),(2,3),(3,4),(4,5),(3,5),(4,5)]

#L.sort()
#print(L)    #[(1, 2), (2, 1), (2, 3), (3, 4), (3, 5), (4, 5), (4, 5)]

#This sort as per in assending order as per first  element,

#L.sort(reverse=True)
#print(L)           #[(4, 5), (4, 5), (3, 5), (3, 4), (2, 3), (2, 1), (1, 2)]


#but we want assending order as per last element in a tuple.

def first(seq):
    return seq[-1]
print(first((2,5)))

L.sort(key=first)
print(L)


2. WAP to split a list every Nth element.

L=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']

n=int(input("Enter No: "))
p=[]
for i in range(n):
    p.append(L[i::n])
print(p) 


3. WAP to insert a given string at the begining of all items in a list.

L=[1,2,3,4]
s=input("Enter String: ")
p=[]

for i in L:
    p.append(s+str(i))
print(p)


4. WAP to flatten a given nested list structure.

L=[0,10,[20,30],40,50,[60,70,80],[90,100,110,120]]

p=[]

for i in L:
    if type(i)==list:
        p.extend(i)
    else:
        p.append(i)
print(p)

eg.
L=[]
L.extend('hiii')
print(L)         #['h', 'i', 'i', 'i']

also
L=[]
L.extend([1,2,3])
print(L)   #[1, 2, 3]


5. WAP 
'''



    
































