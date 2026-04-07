"""
Question:
Question: Write a program that computes the net amount of a bank account based a transaction log from console
input. The transaction log format is shown as following: D 100 W 200

D means deposit while W means withdrawal. Suppose the following input is supplied to the program:
D 300 D 300 W 200 D 100 Then, the output should be: 500
"""

user = input("Enter a transaction log: ").split()

res = dict({})
for i in range(len(user)):
    if i % 2 != 0:
        continue
    if user[i] in res:
        res[user[i]] += int(user[i+1])
    else:
        res[user[i]] = int(user[i+1])
final = res['D'] - res['W']
print(final)


#chatgpt idea
# user = input("Enter a transaction log: ").split()
# balance = 0
# for i in range(0, len(user), 2):
#     if user[i] == "D":
#         balance += int(user[i+1])
#     elif user[i] == "W":
#         balance -= int(user[i+1])
#
# print(balance)