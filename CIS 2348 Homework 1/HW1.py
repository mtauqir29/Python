"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""

print('Birthday Calculator')
print('current day')
month = int(input('Month:'))
day = int(input('Day:'))
year = int(input('Year:'))
print('Birthday')
B_month = int(input('Month:'))
B_day = int(input('Day:'))
B_year = int(input('Year:'))
age = 0
if month > B_month:
    if day >= B_day:
        age = year - B_year
        age = age + 1
elif day == B_day and month == B_month:
        age = year - B_year
        print('Happy Birthday!')
else:
    age = year - B_year
    age = age - 1

print('You are', age, 'years old.')