'''

Set: It is immutable , UNoredered collection of data. sets are ITERABLE & CONTAINS UNIQUE ELEMENT(NO DUPLICATE)


Two types: Set and Frozenset


Basic operations:  (NO INDEXING, HASHING, SLICING, STRIDING, CONCATENATION AND REPLICATION IS ALLOWED)

1. Empty set:

s=set()

s1=frozenset()


2. set with elements:

s=set([1,2,3,4,4])
print(s)                 #{1, 2, 3, 4}

or

s={1,2,3,4,5,1,2,3,4}
print(s)                 #{1, 2, 3, 4, 5}

or

S='HELLOPYTHON'
s=set(S)
print(s)             #{'P', 'L', 'N', 'O', 'T', 'E', 'H', 'Y'}


3. Iterations:

s={1,2,3,5,6,'hi','hello',10.3}
for i in s:
    print(i)     #as it is unorderd, so any result can come.



4. Membership: (in,not)

s={1,2,3,5,6,'hi','hello',10.3}

print(6 in s)
print('hi' in s)


METHODS OF SET:

1. add: We can add one element at a time.

s={1,2,3,5,6,'hi','hello',10.3}
s.add(7)
print(s)

s.add('welcome')
print(s)


2.clear():
s=set([1,2,3,4,5,'hi', 'hello'])
s.clear()
print(s)


s={1,2,3,4,5,'hi', 'hello'}
s.clear()
print(s)


3. difference(s):It finds different elements from first set.

s1={1,2,3,4,5,'hi', 'hello'}
s2={2,3,4,'welcome',5,6,7}

print(s1.difference(s2))
print(s1-s2)


4. difference_update(-=):

s1={1,2,3,4,5,'hi', 'hello'}
s2={2,3,4,'welcome',5,6,7}

s1.difference_update(s2)
print(s1)

s2.difference_update(s1)
print(s2)


5. symmetric_difference(^): It finds different elements from both sets.
s1={1,2,3,4,5,'hi', 'hello'}
s2={2,3,4,'welcome',5,6,7}

print(s1^s2)


6. symetric_difference_update(^=)

s1={1,2,3,4,5,'hi', 'hello'}
s2={2,3,4,'welcome',5,6,7}

s1^=s2
print(s1)

7.Intersection(&): It finds common elements between two sets.

s1={1,2,3,4,5,'hi', 'hello'}
s2={2,3,4,'welcome',5,6,7}

print(s1&s2)


8. Intersection_update(&=):

s1={1,2,3,4,5,'hi', 'hello'}
s2={2,3,4,'welcome',5,6,7}

s1&=s2
print(s1)


9. Union (|): It combines unique elements from sets.

s1={1,2,3,4,5,'hi', 'hello'}
s2={2,3,4,'welcome',5,6,7}

print(s1|s2)


10. Union_update(|=):

s1={1,2,3,4,5,'hi', 'hello'}
s2={2,3,4,'welcome',5,6,7}

s1|=s2
print(s1)

11. remove(): first give command and then print. 

s1={1,2,3,4,5,'hi', 'hello'}
s1.remove(1)
print(s1)


12. pop(): It removes random element.

s1={1,2,3,4,5,'hi', 'hello'}
s1.pop()
print(s1)
s1.pop()
print(s1)


13. discard():

s1={'hi', 'hello', 101, 20, 21,1,2,3,4}
s1.discard(20)
print(s1)


TO CHECK TRUE AND FALSE:

14. isdisjoint(): It mentions TRUE OR FALSE, if sets contains same elements it shows false, else true. 

s1={1,2,3,4}
s2={2,1,3,4}
s3={'hi', 'hello', 101, 20, 21}
s4={2,1,3,4}

print(s1.isdisjoint(s2))      #False
print(s1.isdisjoint(s4))      #False
print(s1.isdisjoint(s3))      #True


15. issubset():

s1={1,2,3,4}
s2={2,1,3,4,5,6,7}
s3={'hi', 'hello', 101, 20, 21}
s4={2,1,3,4}

print(s1.issubset(s2))      #True    
print(s1.issubset(s4))      #True 
print(s1.issubset(s3))      #False


16. issuperset():

s1={1,2,3,4}
s2={2,1,3,4,5,6,7}
s3={'hi', 'hello', 101, 20, 21}
s4={2,1,3,4}

print(s1.issuperset(s2))      #Fasle    
print(s1.issuperset(s4))      #True 
print(s1.issuperset(s3))      #False
print(s2.issuperset(s1))      #True
print(s2.issuperset(s4))      #True


Few Examples:
1. WAP to create a set.

Empty set:
s=set()    

Set with elements:
s={1,2,3,4}

Set from string:
s='hhacahdakjkj'
s1=set(s)
print(s1)


2. WAP to iterate over set.

s='hhacahdakjkj'
s1=set(s)
print(s1)
for i in s1:
    print(i)


s1={1,2,3,4,5,6,6,7,8,'hi'}
for i in s1:
    print(i)


3. WAP to add members in a set.

s1={1,2,3,4,5,6,6,7,8,'hi'}
s1.add('welcome')
print(s1)


4. WAP to remove items from set.

s1={1,2,3,4,5,6,6,7,8,'hi'}
s1.remove('hi')
print(s1)


5. WAP to create inersection of elements.

s1={1,2,3,4,4}
s2={2,3,4,5,6,7}
print(s1&s2)


s1='Pyhton'
s2='Programming'
a=set(s1)
b=set(s2)
print(a&b)


6. WAP to find common characters between two stings using sets.

s1='My name is Firoj'
s2='I am a Teacher'

a=set(s1)
b=set(s2)
print(a.intersection(b))

c=a&b
s3="".join(c)
print(s3)


7. WAP to find distict characters between two strings.

s1='My name is Firoj'
s2='I am a Teacher'

a=set(s1)
b=set(s2)

c=a-b
print(c)     #{'j', 'y', 'o', 'M', 'n', 's', 'i', 'F'}   difference

d=(a^b)
print(d)     #{'c', 'j', 'T', 'y', 'o', 'h', 'M', 'I', 'n', 's', 'i', 'F'}      symmetric_difference

print("".join(d))     #iMjsFTnoyIch


8. WAP to insert squares of nos between (1,21) into sets.

L=[]
for i in range(1,21):
    L.append(i*i)
s=set(L)
print(s)


OR


s=set()
for i in range(1,21):
    s.add(i*i)
print(s)


'''

##s1='My name is Firoj'
##s2='I am a Teacher'

    


















