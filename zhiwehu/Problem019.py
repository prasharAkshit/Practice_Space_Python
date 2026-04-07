"""
Questions:
You are required to write a program to sort (name, age, height) tuples in ascending order.
Name is a string, Age and Height are numbers
Sorting Criteria (Priority Order):
Sort by Name
Then by Age
Then by Height
👉 Priority: Name > Age > Height
Input Format:
Tuples are entered via console as space-separated values:
Tom,19,80
John,20,90
Jony,17,93
Jony,17,91
Json,21,85


Expected Output:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""

result = []
while True:
    str = input()
    if str == '':
        break
    inlist = str.split(',')
    result.append(inlist)

result = sorted(result, key=lambda x: (x[0], x[1], x[2]))
print(result)