"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""

numbers = input("")

old_list = numbers.split()

list = ([])

for x in old_list:

   if int(x) >= 0:

       list.append(int(x))

list.sort()

for y in list:

   print(y, end=" ")
