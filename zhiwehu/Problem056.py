"""
Questions: Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

try:
    print(5/0)
except ZeroDivisionError:
    print("Division by zero")
except Exception as e:
    print(e)
finally:
    print("finally Would always run.")