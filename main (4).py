#1.1 Implement a recursive function to calculate the factorial of a given number.
def fact(n):
    """This is a recursive function
    to find the factorial of an integer"""

    if n == 0:
        return 1
    else:
        return (n * fact(n-1))
print(fact(5))