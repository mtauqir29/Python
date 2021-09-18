"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""
import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_width * wall_height
print('Wall area:', wall_area, 'square feet')

# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
gallon = float(350)
g_paint = float(wall_area / gallon)
print('Paint needed:', '{:.2f}'.format(g_paint), 'gallons')

# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
cans = round(g_paint)
print('Cans needed:', cans, 'can(s)')
print('')
# FIXME (4): Calculate and output the total cost of paint can needed depending on color
color = str(input('Choose a color to paint the wall:\n'))
cost = paint_colors.get(color) * cans
print('Cost of purchasing ', color, ' paint: $', cost, sep='')