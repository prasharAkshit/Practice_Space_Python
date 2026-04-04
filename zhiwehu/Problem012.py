"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
final_list = []
for i in range(1000, 3001):
    even = True

    for j in list(str(i)):
        if int(j)%2!=0:
            even = False
            break
    if even:
        final_list.append(str(i))

print(",".join(final_list))