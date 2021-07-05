'''
Data Structure: It is the way to store Data.

Two types: 1. Mutable and 2. Immutable

Mutable: We can edit it. eg. List, Dictionary

Immutable: Once declared, we cannot edit. eg. String, Tuple, Set: a. Set(Mutable) and b. Frozenset(Immutable)


A. List:

Operations on List:

a. Empty List:
    L=[]

b. List with elements:
    L= [12, 13, 24, 24.5, 7.5, 'Hello', '10', [1,2,3]]

c. Indexing:
         0   1   2    3    4      5       6        7
    L= [12, 13, 24, 24.5, 7.5, 'Hello', '10', [1,2,3]]
        -8   -7  -6  -5   -4     -3      -2      -1

d. Hashing:
      syntax: seq_name[index_no.]

      L= [12, 13, 24, 24.5, 7.5, 'Hello', '10', [1,2,3]]

      print(L[1])
      print(L[5])
      print(L[-3])

e. Iteration:
      i. using elements:
        for i in L:
             print(i)

    ii. using indexes of elements:
        for i in range(len(L)):
            print(L[i])

f. List updation:
      i. Add new element:
        syntax: seq_name[valid index no.]= new value

        L= [12, 13, 24, 24.5, 7.5, 'Hello', '10', [1,2,3]]

            L[2]='hii'
            print(L)        

      ii. Deleting element:
         syntax: del[index no.]

            L= [12, 13, 24, 24.5, 7.5, 'Hello', '10', [1,2,3]]

            del L[3]
            print(L)

g. Concatenation: Data type should be of same type.
        L1=[1,2,3,4,5,6]
        L2=['hi', 'hello', 'bye', 'welcome']

        print(L1+L2)

h. Replication: Multiplier should be integer.

        L1=[1,2,3,4,5,6]
        L2=['hi', 'hello', 'bye', 'welcome']

        print(L1*3)   #[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
        print(L2*5)   #['hi', 'hello', 'bye', 'welcome', 'hi', 'hello', 'bye', 'welcome', 'hi', 'hello', 'bye', 'welcome', 'hi', 'hello', 'bye', 'welcome', 'hi', 'hello', 'bye', 'welcome']


i. Stepping:
        L1=[1,2,3,4,5,6]
        L2=['hi', 'hello', 'bye', 'welcome']

        print(L1[0:6:2])

        print(L2[1:5:2])
'''
























