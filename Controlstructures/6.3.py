###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = input('Switch 1 on? (Y/N): ') == 'Y'
light_switch2 = input('Switch 2 on? (Y/N): ') == 'Y'
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2
print(f'Bulbs on: {bulbs_on}')