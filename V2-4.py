
'''
1. PRINT FUNCTION IN PYTHON:

print('hello', 'welcome')
print('to', 'python', 'class')
#here by default it will take space between two values and new line between two print function


print('hello', 'welcome', end=' ')
print('to', 'python', 'class')
# here we can change end as per our requirement, by addind end=' ' 


print('hello', 'welcome', end=' ')
print('to', 'python', 'class', sep=',')
# here you can change sep as per our requirement by writing it. By default sep as SPACE is present.

2. KEYWORDS IN PYTHON: RESERVED WORDS

import keyword
print(keyword.kwlist)  #you will get list of keyword in Python
print(len(keyword.kwlist))
print(dir(keyword.kwlist))
print(len(dir(keyword.kwlist)))


3. BASIC CONCEPTS IN PYTHON:

A. INDEXING:
    +indexing: strats from 0
    -indexing: starts from -1
              0 1 2 3 4 5 
          s= 'P y t h o n'
             -6-5-4-3-2-1      


B. HASHING:

s='Pyhton'
print(s[0])
print(s[-6])
print(s[4])
print(s[7])    

C. SLICING:

s='Python'
print(s[0:4])
print(s[3:])
print(s[:])
print(s[:-3])
print(s[5:4])

D. STRIDING/STEPPING:

s='Python'
print(s[0:5:2])
print(s[0:7:3])
print(s[5:0:-2])
print(s[::-1])

#E. MEMBERSHIP:

s='Python'
print('o' in s)
print('p' in s)

#F. CONCATENATION:

s1='Hi'
s2='Hello'
s3='303'

print(s1+s2)
print(s1+' '+s2)
print(s1+s2+s3)
print(s1+s2+100)   # error will occur, As datatype should be same.

#G. REPLICATION:

s1='Firoj'
print(s1*3)
print(s1*s1)   # multiplier should be integer

#H. TYPECASTING:

s='100'
print(int(s))

n=200
s1=str(n)
print(s1)

s='Hello'
print(list(s))



#I. CHARACTER TO ASCII NUMBER:

print(ord('a'))
print(ord('D'))

#J. ASCII TO CHARACTER NUMBER:

print(chr(97))
print(chr(22))

'''








































