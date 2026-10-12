print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def f(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

print(f(20))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def factor(a,b):
    if a % b == 0 or b % a == 0:
        return True
    else:
        return False

print(factor(20,10))
print(factor(15,10))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

def letter(x):
    return alphabet.index(x)

print(letter("z"))
print(letter("h"))



print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def nameid(name):
    result = ""
    for character in name:
        pos = alphabet.index(character)
        result = result + str(pos)
    return result

print (nameid("saif"))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def password(name):
    id = ""
    for character in name:
        pos = alphabet.index(character)
        id = id + str(pos)
    sum_of_digits = 0
    for digit in id:
        sum_of_digits = sum_of_digits + int(digit)


    return int(id) - sum_of_digits
print (password("saif"))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False

    return is_prime

print(prime(7))
print(prime(9))


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def prime(number):
    if type(number) != int:
        return False

    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True