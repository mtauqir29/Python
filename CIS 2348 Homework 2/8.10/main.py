"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""

word = input()
normal_word = ""
reverse_word = ""

for i in range(len(word)):
   if word[i].isalpha():
       normal_word += word[i].lower()
       reverse_word = word[i].lower() + reverse_word

if normal_word == reverse_word:
   print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")