"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class atleast:
    def __init__(self):
        self.i = ""

    def getString(self):
        self.i = str(input("Enter a string: "))

    def printString(self):
        print((self.i).upper())

a = atleast()
a.getString()
a.printString()