'''
STRING: IT IS AN ORDERED COLLECTION OF IMMUTABLE DATA, WHICH IS ITERABLE ,
        HASHABLE.
        WE USE SINGLE QUOTES OR DOUBLE QUOTES.

OPERATIONS:
1. Empty string:

s=' '  or  ''   ''

2. String with single element:

s='Hello'   or  s="Hello"

3. String with multiple elements: use three qoutes '''  '''

4. Iterations:
for i in s:
    print(i)

P
y
t
h
o
n
 
W
o
r
l
d



Methods of string:

1. capitalize(): Only capitalize first word of sentenance.

s='hello python world'
s.capitalize()    #'Hello python world'

2. count():
>>> s='hello python world'
>>> s.count('l')
3
>>> s.count('l',0,6)
2
>>> s.count('l',0,5)
2
>>> s.count('l',0,4)
2

3. endswith():
s='hello python world'
>>> s.endswith('n')
False
>>> s.endswith('d')
True


4. startswith():
s='hello python world'
>>> s.startswith('h')
True
>>> s.startswith('p',6)
True


5. For checking true and flase , some methods are used:
a. isalnum(): aplha-numeric values only, no special characters.
b. isalpha(): alpha values only
c. isdigit(): numeric values only
d. islower(): lower cases only
e. isupper(): upper cases only
f. isspace(): only spaces
g. istitle(): means each word of sentenance starts with capital letter.


6. title(): each letter starts with capital.
>>> s.title()
'Hello Python World'

7. 
'''





























