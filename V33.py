'''
Expression Oriented Programming (EOP):

1. Anonymous Function/Lambda Function: It is the function without name.

Syntax:
        lambda parameters : Expression Condition

NOTE: In lambda function, Dont use FOR AND WHILE loop.

FEW EXAMPLES:
A. ADDITION OF TWO NUMBERS: (Similarly we can perform substraction, multiplication, division)

#Normal Function:

def add(a,b):
    return a+b
print(add(6,7))


#Lambda function:

obj=(lambda a,b:a+b)
print(obj(6,7))


B. MAX AND MIN NUMBER:

#Normal Function:
def max_no(a,b):
    if a>b:
        return(f"{a} is max number")
    else:
        return(f"{b} is max number")
print(max_no(5,14))

#Lambda function:
obj=lambda a,b:f"{a} is max number" if a>b else f"{b} is max number"
print(obj(5,14))
print(obj(15,14))


C. If-elif-else:

##n%3=0>Buzz
##n%5=0>Fizz
##n%3 and 5=0>FizzBuzz

#Normal Function:

n=int(input("Enter Number: "))

def isdiv(n):
    if n%3==0 and n%5==0:
        return ("FizzBuzz")
    elif n%3==0:
        return ("Buzz")
    elif n%5==0:
        return ("Fizz")
    else:
        return n
print(isdiv(n))


#Lambda Function:

isdiv=lambda n:"FizzBuzz" if n%3==0 and n%5==0 else "Buzz" if n%3==0 else "Fizz" if n%5==0 else n
print(isdiv(int(input("Enter Number: "))))


D. Find Cube of number:

#Normal Function:
n=int(input("Enter Number: "))
def cube(n):
    return n*n*n
print(cube(n))


#Lambda Function:

cube=lambda n:n*n*n
print(cube(n))


FEW EXPAMLES FROM w3resources:

1. 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.

n=int(input("Enter Number: "))
def add(n):
    return n+15
print(add(n))

OR
add=lambda n:n+15
print(add(n))


AND

obj=lambda x,y:x*y
print(obj(5,6))


2. Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number.

n=int(input("Enter Number: "))
obj=lambda n:n*15
print(obj(n))


3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


L=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

L.sort(key=lambda x:x[1])    #means sort as per first element.
print(L)     #[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


4. Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]


L=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

L.sort(key=lambda x:x['color'])
print(L)


5. Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]

'''
















































