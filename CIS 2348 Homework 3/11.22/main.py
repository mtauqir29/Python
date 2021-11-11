"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""

list_words = input()
list = list_words.split()

for word in list:
        frequency=list.count(word)
        print(word, frequency)