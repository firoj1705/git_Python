'''
Tuple:
It is ordered collection of ITERABLE AND HASHABLE and contains of any kind of data. Similar to list, but it is immutable.

Operations: All opertions can be performed same as list, but updation only not possible, as it is immutable.

1. Empty tuple:

t=()  # called paranthesis.

2. Tuple with single elements:

t=(12,)   #t=(12) can not write like that, trailing comma is must.

3. Tuple with multiple elements:

t=(12,2,3,3,4,5,6)

4. Indexing:
    0 1 2 3 4 5 6
t=(12,2,3,3,4,5,6)
   -7 -6-5-4-3-2-1

5. Hashing:
syntax: seq_name[index no.]
t=(12,2,3,3,4,5,6)
print(t[0])
print(t[-1])

6. Slicing:
syntax: seq_name[start:end]    (end value-1)
t=(12,2,3,3,4,5,6)
print(t[0])
print(t[-1])

7. Stepping:
syntax: seq_name[start:end:step]
t=(12,2,3,3,4,5,6)
print(t[0:5:2])
print(t[5:0:-1])
print(t[::-1])

8. Iteration:
t=(12,2,3,3,4,5,6)
for i in t:
    print(i, end=',')

t=(12,2,3,3,4,5,6)
for i in range(len(t)):
    print(t[i])

9. Membership(in, not):

t=(12,2,3,3,4,5,6)
print(12 in t)
print(7 in t)

10. Replication: Mltiplier should be integer.

t=(12,2,3,3,4,5,6)
print(t*3)

11. Concatenation: Data type should be same type.
t1=(12,2,5,6)
t2=('Hi', '10',3 ,3)
print(t1+t2)


Methods:
1.Count:
t=(12,2,3,3,4,5,6)
print(t.count(2))
print(t.count(3))

2. Index:
t=(12,2,3,3,4,5,6)
print(t.index(12))
print(t.index(6))
print(t.index(1))    #valueError


Problems:

1. WAP to insert list of tuples containing no, square of that no. of range (1,21).

L=[]

for i in range(1,21):
    L.append((i,i*i))
print(L)


2. WAP to count no. of occurences values in given tuple and return as list tuple containing
value, occurences of that value.

t=(1,2,3,4,4,1,2,10,11,11)

L=[]

for i in t:
    if (i,t.count(i)) not in L:       #added this line to avoid double occurences.
        L.append((i,t.count(i)))
print(L)

'''


















































































