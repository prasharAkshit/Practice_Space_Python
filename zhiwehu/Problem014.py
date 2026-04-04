"""
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
"""

user_input = input("Enter a sentence: ")

result = {"upper":0, "lower":0}
for i in user_input:
    if i.isupper():
        result["upper"] += 1
    elif i.islower():
        result["lower"] += 1

print(f"UPPER CASE : {result['upper']} LOWER CASE : {result['lower']}")

