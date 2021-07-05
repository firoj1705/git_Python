'''
Methods of List:

1. Append: to add any value at the end.

L=[1,2,3,4]
L.append(5)
print(L)  #L=[1,2,3,4,5]
L.append('Hello')
print(L) #L=[1,2,3,4,5,'Hello']


2. Extend: to add values at end, which are ITERABLE.

L=[1,2,3,4]
L.extend('Hello')
print(L)   #L=[1,2,3,4,'H','e','l','l','o']

L.extend(4)
print(L)    #ValueError- as integer is not iterable.


3. Insert: to add any value, at any place, use insert.

L=[1,2,3,4]
L.insert(2, 20)
print(L)  #L=[1,2,20,3,4]

L.insert(-1, 10)
print(L)    #L=[1,2,20,3,10,4]


4. Remove:  Remove any value from any place.

L=[1,2,20,3,4]
L.remove(3)
print(L)   #L=[1,2,20,4]


5. Reverse: To reverse the list.

L=[1,2,20,3,4]
L.reverse()
print(L)    #[4, 3, 20, 2, 1]


6. Clear(): To clear the list.

L=[1,2,20,3,4]
L.clear()
print(L)


7. Sort:

L=[1,2,5,7,8,2,20,3,4]
L.sort()
print(L)    #[1, 2, 2, 3, 4, 5, 7, 8, 20]


L=[1,2,5,7,8,2,20,3,4]
L.sort(reverse=True)    #[20, 8, 7, 5, 4, 3, 2, 2, 1]
print(L)


If List contains different datatypes, then covert all DT in one format i.e. string format, as we can convert integer to string easily.
L=[1,2,5,'7',8,'Hi','Hell0',2,20.4,'3.4',3,4]
L.sort(key=str)
print(L)   #[1, 2, 2, 20.4, 3, '3.4', 4, 5, '7', 8, 'Hell0', 'Hi']   We will get output as per ASCII number.


8. Count:

L=[1,2,5,7,8,2,20,3,4]
print(L.count(5))
print(L.count(3))


9. Index (value, index):

L=[1,2,5,7,8,2,20,3,4]
print(L.index(5))
print(L.index(5,3))    # ValueError


10. pop(index=-1, by default):

L=[1,2,5,7,8,2,20,3,4]

print(L.pop(5))      #2
print(L.pop())       #4
'''










































