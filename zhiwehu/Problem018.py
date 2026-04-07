"""
Question:
Question: A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords
and will check them according to the above criteria.
Passwords that match the criteria are to be printed,
each separated by a comma. Example If the following passwords are given as input to the program:
ABd1234@1,aF1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1
"""

user_input = input("Enter a sequence of comma separated passwords: ").strip().split(",")
valid = []
for i in user_input:
    lower = [j for j in i if j.islower()]
    upper = [j for j in i if j.isupper()]
    numeric = [j for j in i if j.isnumeric()]
    special = [j for j in i if not j.isalnum()]

    if 6 < len(i) < 12 and lower != [] and upper != [] and numeric != [] and special != []:
        valid.append(i)

print(", ".join(valid))
