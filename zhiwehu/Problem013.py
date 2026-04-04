"""
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3
"""
num = alpha =0
user_input = input("Please enter a sentence: ")
for i in user_input:
    if i.isdigit():
        num += 1
    elif i.isalpha():
        alpha += 1

print(f"LETTERS {alpha} DIGITS {num}")