"""
Questions:
Write a function that computes the square of a number using recursion.
"""

def square(n):
    if n == 0:
        return 0
    return square(n - 1) + 2*n - 1

print(square(3))