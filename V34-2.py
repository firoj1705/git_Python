'''
EOP Continue.........


3. enumerate(iterable, start): With this we can get list or dictionary of 2-tuples from iterables like string, list, set etc. 

s='abcde'

e1=list(enumerate(s))
print(e1)  #[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]


e1=list(enumerate(s,15))
print(e1)    #[(15, 'a'), (16, 'b'), (17, 'c'), (18, 'd'), (19, 'e')]


e1=dict(enumerate(s,11))
print(e1)    #{11: 'a', 12: 'b', 13: 'c', 14: 'd', 15: 'e'}


s1={1,2,3,4,6,8,9,4,3}
e2=list(enumerate(s1))
print(e2)   #[(0, 1), (1, 2), (2, 3), (3, 4), (4, 6), (5, 8), (6, 9)] as in set repeatation is not allowed.


L=[1,2,3,4,5,5,5,56,6,7]

e3=dict(enumerate(L,3))
print(e3)    #{3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 5, 9: 5, 10: 56, 11: 6, 12: 7}


4. zip(*iterables): We can combine number of iterables. Ouput will be list of tuple.

s='abcde'
L=[1,2,3,4,5,5,5,56,6,7]
s1='hdadsjksjkaj'

z1=list(zip(s,L,s1))
print(z1)  #[('a', 1, 'h'), ('b', 2, 'd'), ('c', 3, 'a'), ('d', 4, 'd'), ('e', 5, 's')]


s3=''
z2=list(zip(s,L,s1,s3))
print(z2)    #[] as s3 is empty so result also empty.


d={'a':10, 'b':23, 'c':'fff', 'd':45}
z3=list(zip(s,L,s1,d))
print(z3)     #[('a', 1, 'h', 'a'), ('b', 2, 'd', 'b'), ('c', 3, 'a', 'c'), ('d', 4, 'd', 'd')]


5. map(): Use lambda fucntion in this, except length of function.

s='abcde'
L=[1,2,3,4,5,5,5,56,6,7]

m1=list(map(lambda x,y:x+str(y), s,L))
print(m1)    #['a1', 'b2', 'c3', 'd4', 'e5']


s1='i am a teacher'
m2=list(map(lambda x:x.title(),s1))
print(m2)
s2="".join(m2)
print(s2)

L1=['my', 'name' ,'is', 'fst']
m3=list(map(lambda x:x.title(),L1))
print(m3)


L1=['my', 'name' ,'is', 'fst']
m3=list(map(lambda x:x.title(),L1))
print(m3)             #['My', 'Name', 'Is', 'Fst']


L1=['my', 'name' ,'is', 'fst']
m4=list(map(lambda x:x.upper(),L1))
print(m4)   #['MY', 'NAME', 'IS', 'FST']


m5=list(map(len,L1))
print(m5)        #[2, 4, 2, 3]


6. filter(function , iterable): here only single iterable we can give.

L=[5,7,8,9,9,5,43,3,-1,-5,-18, -14, -17, 64, 374, 75]
f1=list(filter(lambda x:x%2==0, L))
print(f1)          #[8, -18, -14, 64, 374]


f1=list(filter(lambda x:x%2==0 and x>0, L))
print(f1)      #[8, 64, 374]



L1=['hi', 'hello', 'welcome', 'My', 'Python', 'End']

f2=list(filter(lambda x:len(x)>3, L1))
print(f2)    #['hello', 'welcome', 'Python']

f3=list(filter(lambda x:x.istitle(), L1))
print(f3)       #['My', 'Python', 'End']

f4=list(filter(lambda x:x.islower(), L1))
print(f4)    #['hi', 'hello', 'welcome']

f5=list(filter(lambda x:x.isalpha(), L1))
print(f5)     #['hi', 'hello', 'welcome', 'My', 'Python', 'End']


7. functools.reduce()

import functools
L=[5,7,8,9,9,5,43,3,-1,-5,-18, -14, -17, 64, 374, 75]

r1=functools.reduce(lambda x,y:x+y, L)
print(r1)            #547


r2=functools.reduce(lambda x,y:x+y, L, 10)
print(r2)            #557


r2=functools.reduce(lambda x,y:x+y, range(1,21), 10)
print(r2)     #220


r2=functools.reduce(lambda x,y:x+y, range(1,21), 10)
print(r2)

'''



























































