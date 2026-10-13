print("\nQ1a\n")
# Q1a: Replicate the following functions as lambda functions


def square(n):
    return n*n

square = lambda n: n * n

def percentage(n):
    return n/100

divide = lambda n : n/100

def multiplier(n, m):
    return n*m

multi = lambda n,m: n*m

def addition(a, b, c):
    return a + b + c
add = lambda a,b,c : a+b+c

# A1a:


print("\nQ1b\n")
# Q1b: Write an explanation of how this factorial lambda function works
factorial = lambda a: a*factorial(a-1) if (a>1) else 1
# this lambda function works by using the variable a and multiplying by a-1 if a is greater than 1 otherwise returns just 1
# A1b:


print("\nQ1c\n")
# Q1c: Using the Map function alongside a lambda function, take the list_of_numbers
# and generate a list of all of the numbers squared
list_of_numbers = [23, 345, 45, 76, 87, 4, 2, 0]

# A1c:

squared_list = list(map(lambda n: n*n, list_of_numbers))
print(squared_list)