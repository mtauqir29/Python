"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""
# part 1
lemon = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
nectar = float(input('Enter amount of agave nectar (in cups):\n'))
serving = float(input('How many servings does this make?\n'))
print('')
print('Lemonade ingredients - yields', '{:.2f}'.format(serving), 'servings')
print('{:.2f}'.format(lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(nectar), 'cup(s) agave nectar')
print('')
# part 2
make_serving = float(input('How many servings would you like to make?\n'))
print('')
new_serving = float(make_serving/serving)
n_lemon = float(lemon * new_serving)
n_water = float(water * new_serving)
n_nectar = float(nectar * new_serving)
print('Lemonade ingredients - yields', '{:.2f}'.format(make_serving), 'servings')
print('{:.2f}'.format(n_lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(n_water), 'cup(s) water')
print('{:.2f}'.format(n_nectar), 'cup(s) agave nectar')
print('')
# part 3
print('Lemonade ingredients - yields', '{:.2f}'.format(make_serving), 'servings')
gallon = float(16)
g_lemon = float(n_lemon / gallon)
g_water = float(n_water / gallon)
g_nectar = float(n_nectar / gallon)
print('{:.2f}'.format(g_lemon), 'gallon(s) lemon juice')
print('{:.2f}'.format(g_water), 'gallon(s) water')
print('{:.2f}'.format(g_nectar), 'gallon(s) agave nectar')


