"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""

pswd = input()
result = ''

i = 0
while i < len(pswd):
    old_pswd = pswd[i]
    if old_pswd == 'i':
        result += '!'
    elif old_pswd == 'a':
        result += '@'
    elif old_pswd == 'm':
        result += 'M'
    elif old_pswd == 'B':
        result += '8'
    elif old_pswd == 'o':
        result += '.'
    else:
        result += old_pswd
    i += 1

result += "q*s"
print(result)