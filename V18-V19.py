'''
Some remaining Methods of string:

1. strip():    removes unwanted space.

s="          @@hello         "
s1=s.strip()
print(s1)


2. split():

s="My name is firoj tanekhan, and i am a teacher"
##L=s.split()
##print(L)      ['My', 'name', 'is', 'firoj', 'tanekhan,', 'and', 'i', 'am', 'a', 'teacher']


##L1=s.split('e')
##print(L1)  #['My nam', ' is firoj tan', 'khan, and i am a t', 'ach', 'r']


##L2=s.split(maxsplit=2)
##print(L2)


L3=s.split('x')
print(L3)     #['My name is firoj tanekhan, and i am a teacher']

3. join()

s="My name is firoj tanekhan, and i am a teacher"
##if i want to update it as a that, i am not teacher and i am engineer
## so we cant update string as it is immutable

L=s.split()
print(L)

L[-1]='engineer'

s1=" ".join(L)
print(s1)

4. Format():

##advanced string formating is:

for i in range(1,21):
    print(f"The sqaure of {i} is {i*i}")


FEW EXAMPLES:

1. WAP to find maximum length word from the given string.

s="the quick brown fox jumps over lazy dog"
L=s.split()

s1=" "
c=0

for i in L:
    if len(i)>=c:
        c=len(i)
        s1=i
print(f"Maximum length word is `{s1}` and its length is `{c}`")

2. WAP to find vowels in given string and its total count.

s="the quick brown fox jumps over lazy dog"
s1=" "
for i in s:
    if i in 'aeiouAEIOU':
        s1=s1+i
print(f"Vowels in given string are {s1} and its count is {len(s1)}")


3. WAP to find maximum occured vowel and its count.

s="the quick brown fox jumps over lazy dog"
s1=" "
for i in s:
    if i in 'aeiouAEIOU':
        s1=s1+i
print(f"Vowels in given string are {s1} and its count is {len(s1)}")

s2=""
c=0

for i in s1:
    if s1.count(i)>=c:
        c=s1.count(i)
        s2=i
print(f"Maximum occured vowel is `{s2}` and its count is `{c}`")


4. WAP to reverse a string by words that are the last word becomes first and vice versa.

s="the quick brown fox jumps over lazy dog"

L=s.split()
L.reverse()
print(L)

s1=" ".join(L)
print(s1)


5. WAP to reverse a word on its own position.

s="the quick brown fox jumps over lazy dog"

L=s.split()
L1=[]
for i in L:
    L1.append(i[::-1])
print(L1)

s1=" ".join(L1)
print(s1)

Solution 2:
s="the quick brown fox jumps over lazy dog"

L=s.split()
for i in range(len(L)):
    L[i]=L[i][::-1]
s1=" ".join(L)
print(s1)

    
6. WAP to print a specified list after removing the 0th, 4th and 5th elements.
L=["red","green","white","black","pink","yellow"]

L.remove(L[0])
L.remove(L[3])
L.remove(L[3])
print(L)


7. WAP to add 'ly' if string endswith 'ing', otherwise add 'ing' if string is not ending with 'ing'.

s=input("Enter string: ")

if s.endswith('ing'):
    s=s+'ly'
else:
    s=s+'ing'
print(s)


8. WAP to count no. of individual character from given string and return list of tuple containing
(character, count of that char.) 

s='the quick brown fox jumps over lazy dog'
L=[]
for i in s:
    if not i.isspace():
        if (i,s.count(i)) not in L:
            L.append((i,s.count(i)))
print(L)


9. WAP to find a maximum occured character from the given string.

s='the quick brown fox jumps over lazy dog'

s1=''
c=0
for i in s:
    if not i.isspace():
        if i in 'abcdefghijklmnopqrstuvwxyz':
            s1=s1+i
print(s1)                                            not possible
        

10. Write a Python program to capitalize first and last letters of each word of a given string.
'''
s='the quick brown fox jumps over lazy dog'



        

























































