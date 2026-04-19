""""
Question: Define a function which can generate a list where
the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the last 5 elements in the list.
"""

def Sq_list():
    square_list = [i**2 for i in range(1,21)]

    for i in square_list[-5:]:
        print(i)

Sq_list()
