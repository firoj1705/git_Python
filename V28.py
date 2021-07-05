'''
Dictionary: It is an UNORDERED MUTABLE data collection. Contains Key, Value Pairs.
             Key is a unique (No duplicate). KEY SHOULD BE IMMUTABLE. LIST CAN not BE A KEY.



Operations on Dictionary: NO SLICING, STRIDING, CONCATENATION, REPLICATION IS PERFORMED ON DICTIONARY.

1. Empty Dictionary:

d={}


2. Dictionary with elements:

d={'a':10,'b':29,'c':31,'d':25,'e':12}


3. Iteration on key:

d={'a':10,'b':29,'c':31,'d':25,'e':12}

for i in d:
    print(i)         #Output is only key.


4. Hashing: Key only key

d={'a':10,'b':29,'c':31,'d':25,'e':12}

print(d['a'])    #10
print(d['e'])    #12


5. Membership:  Give Only Key.

d={'a':10,'b':29,'c':31,'d':25,'e':12}

print('a' in d)    #True
print(12 in d)     #False
print('f' not in d)  #True


6. Updation:

d={'a':10,'b':29,'c':31,'d':25,'e':12}

d['e']=20
print(d)     #{'a': 10, 'b': 29, 'c': 31, 'd': 25, 'e': 20}

d['c']=10
print(d)     #{'a': 10, 'b': 29, 'c': 10, 'd': 25, 'e': 20}  

d['f']=13
print(d)     #{'a': 10, 'b': 29, 'c': 10, 'd': 25, 'e': 20, 'f': 13}


7. Deletion:

d={'a':10,'b':29,'c':31,'d':25,'e':12}

del d['a']
print(d)       #{'b': 29, 'c': 31, 'd': 25, 'e': 12}

del d['f']
print(d)          #keyError



METHODS OF DICTIONARY:

1. clear():

d={'a':10,'b':29,'c':31,'d':25,'e':12}
d.clear()
print(d)


2. items(): It gives LIST OF TUPLE (KEY, VALUE)


d={'a':10,'b':29,'c':31,'d':25,'e':12}

for k,v in d.items():
    print(k,v)

##a 10
##b 29
##c 31
##d 25
##e 12

OR

print(d.items())    #dict_items([('a', 10), ('b', 29), ('c', 31), ('d', 25), ('e', 12)])


3. get(): 

d={'a':10,'b':29,'c':31,'d':25,'e':12}

print(d.get('c'))    #31
print(d.get('f'))    #None


4. keys(): IT GIVES LIST OF KEYS.

d={'a':10,'b':29,'c':31,'d':25,'e':12}
print(d.keys())    #dict_keys(['a', 'b', 'c', 'd', 'e'])


5. values():

d={'a':10,'b':29,'c':31,'d':25,'e':12}
print(d.values())    #dict_values([10, 29, 31, 25, 12])


6. update():

d1={'a':10,'b':29,'c':31,'d':25,'e':12}
d2={'a':20,'f':23,'g':39,'e':19}
d1.update(d2)
print(d1)    #{'a': 20, 'b': 29, 'c': 31, 'd': 25, 'e': 19, 'f': 23, 'g': 39}

d2.update(d1)
print(d2)    #{'a': 10, 'f': 23, 'g': 39, 'e': 12, 'b': 29, 'c': 31, 'd': 25}


FEW EXAPMLES:
1. WAP to insert squares of nos such that original no as key and square of that will be value for that key.

d={}
for i in range(1,21):
    d[i]=i*i
print(d) 


2. WAP to insert word of string as key and its length as value for that key in dict.

s='the quick brown fox jumps over lazy dog'
d={}
L=s.split()
for i in L:
    if not i.isspace():
        d[i]=len(i)
print(d)        #{'the': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumps': 5, 'over': 4, 'lazy': 4, 'dog': 3}    


3. WAP to insert data into dict such that, words first character will be key for that word and value will be
complete word for that key. If more than one word is starting with same character then concenate them.

s='the quick brown fox jumps over that lazy dog'
d={}
L=s.split()
for i in L:
    if i[0] not in d:
        d[i[0]]=i
    else:
        d[i[0]]=d[i[0]]+i
print(d)      #{'t': 'thethat', 'q': 'quick', 'b': 'brown', 'f': 'fox', 'j': 'jumps', 'o': 'over', 'l': 'lazy', 'd': 'dog'}


4.WAP to count no of character in string using dict. Don't count whitespaces.

s='the quick brown fox jumps over lazy dog'
d={}

for i in s:
    if not i.isspace():
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
print(d)     #{'t': 1, 'h': 1, 'e': 2, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1,
                'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1,
                's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}


5. By using problem 4 , WAP to find maximum occured character of the string.

s='the quick brown fox jumps over lazy dog'
d={}

for i in s:
    if not i.isspace():
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
print(d)

s1=''
count=0
for k in d:
    if d[k]>count:
        count=d[k]
        s1=k
print(f"Maximum occured character is:{s1} and its count is:{count}")


6. WAP to find first 10 multipliers of the range(1,11).

d={}

for i in range(1,11):
    L=[]
    for j in range(1,11):
        L.append(i*j)
    d[i]=L
print(d)

for k,v in d.items():
    print(k,v,sep=":")


7. WAP to merge 2 dictionary by adding value of existing key, and add (key, value) pairs if not exist.

d1={'a':123, 'b': 345, 'c':453}
d2={'b':432, 'e':456, 'f': 678}

for i in d2:
    if i not in d1:
        d1[i]=d2[i]
    else:
        d1[i]=d1[i]+d2[i]
print(d1)
     

8. WAP to find vowels present in string using dict and add them into individual list as per vowels.

s='the quick brown fox jums over lazay dog'
d={'a':[],'b':[],'c':[],'d':[]}

for i in s:
    if i in d:
        d[i].append(i)
print(d)


9. WAP to update given dictionary.

d={'id':[],'name':[],'age':[],'salary':[]}

n=int(input("Enter how many enteries you want: "))

for i in range(n):
    for k in d:
        if k=='id' or k=='age':
            d[k].append(int(input("Please enter {k}: ")))
        elif k=='salary':
            d[k].append(float(input("Please enter {k}: ")))
        elif k=='name':
            d[k].append(input("Please enter {k}: "))
        else:
            pass
print(d)                                                              #not solved



PROBLEMS FROM W3RESOURCES:

1. Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}

d={0:10, 1:20}
d[2]=30
print(d)    #{0: 10, 1: 20, 2: 30}  This is update operation.


2.Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
d={}
for i in dic1:
    if i not in d:
        d[i]=dic1[i]
        for j in dic2:
            if j not in d:
                d[j]=dic2[j]
                for k in dic3:
                    if k not in d:
                        d[k]=dic3[k]
print(d)           #{1: 10, 3: 30, 5: 50, 6: 60, 4: 40, 2: 20}

OR

for i in dic1:
    if i not in d:
        d[i]=dic1[i]
for j in dic2:
    if j not in d:
        d[j]=dic2[j]
for k in dic3:
    if k not in d:
        d[k]=dic3[k]
print(d)           #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


4. Write a Python script to check whether a given key already exists in a dictionary.

d1={1:10, 2:20, 3:30, 4:40, 5:50}
d2={10:10, 8:20, 7:30, 4:40, 6:50}

for k in d1:
    if k in d2:
        print("Key already present in d1")
    else:
        print("No key present")


5. Write a Python program to iterate over dictionaries using for loops.

d1={1:10, 2:20, 3:30, 4:40, 5:50}

for i in d1:
    print(i)


6. Write a Python script to generate and print a dictionary that contains
   a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n=int(input("Enter how many entries you want: "))
d={}

for i in range(1,n+1):
    if i not in d:
        d[i]=i*i
print(d)

##Enter how many entries you want: 5
##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


7. Write a Python script to print a dictionary where the keys are numbers
   between 1 and 15 (both included) and the values are square of keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

d={}
for i in range(1,16):
    d[i]=i*i
print(d)


8. Write a Python script to merge two Python dictionaries

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

d1.update(d2)
print(d1)

OR

d1 = {'a': 100, 'b': 200, 'x':200}
d2 = {'x': 300, 'y': 200}

for i in d1:
    if i not in d2:
        d2[i]=d1[i]
    else:
        d2[i]=d2[i]+d1[i]
print(d2)


9. Write a Python program to iterate over dictionaries using for loops.

d = {'Red': 1, 'Green': 2, 'Blue': 3}

for k,v in d.items():
    print(k, "corresponds to", v)


10. Write a Python program to sum all the items in a dictionary. 

d = {'a':100,'b':-2000,'c':5456,'d':1234}
print(sum(d.values()))


11. Write a Python program to multiply all the items in a dictionary.

d = {'a':20,'b':-20,'c':5,'d':12}
c=1

for i in d:
    c=c*d[i]
print(c)


12. Write a Python program to remove a key from a dictionary.

d = {'a':20,'b':20,'c':5,'d':12}
del d['c']
print(d)


'''












 























        




        



























