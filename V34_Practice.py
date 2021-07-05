'''
EOP:

1. Lambda function: Dont use for and while loop.

def add(a,b):
    return a+b
print(add(4,5))


obj=lambda a,b:a+b
print(obj(4,5))


def sum_digit(n):
    if n==0:
        return 0
    else:
        return n%10+sum_digit(n//10)
print(sum_digit(12345))


obj=lambda n:0 if n==0 else n%10+sum_digit(n//10)
print(obj(12345))


2. List comprehension:

syntax 1:
           [exp loop(for) cond]

syntax 2:
           [exp cond loop(for)]



3. enumerate(iterator, start): we can get list or dict of tuples.

s='hello world python'
e1=list(enumerate(s))
print(e1)

e2=dict(enumerate(s,11))
print(e2)


4. zip(*iterables): list of tuple of iterables.

s='hi Python world'
L=[1,2,3,4,5,6,7]

z1=list(zip(s,L))
print(z1)

s1={45,66,7,78,89,99}

z2=list(zip(s,L,s1))
print(z2)


5. map: give lambda function.

s='hi Python world'
L=[1,2,3,4,5,6,7]

m1=list(map(lambda x,y: x+str(y), s,L))
print(m1)

m2=list(map(lambda x:x.title(), s))
print(m2)


6. filter(iterable):

L=[1,2,3,4,5,6,7]
        
f2=list(filter(lambda x: x%2==0, L))
print(f2)


L1=['hahs', 'ahjasj', 'shgdhgSSADJ', 'GASDGsg']
f3=list(filter(lambda x: len(x)>4, L1))
print(f3)


7. functools.reduce():


'''

import functools

L=[1,2,3,4,6,7,8,99,0]

r1=functools.reduce(L)
print(r1)




























