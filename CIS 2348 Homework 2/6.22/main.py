"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""

first = int(input())
second = int(input())
third = int(input())

fourth = int(input())
fifth = int(input())
sixth = int(input())

solution = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if first * x + second * y == third and fourth * x + fifth * y == sixth:
            print(x, y)
            solution = True

if not solution:
    print("No solution")