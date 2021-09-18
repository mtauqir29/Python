"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""

services = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12
}
# 1. Menu
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print('')
# 2. Prompt the user for two services from the menu
f_service = str(input('Select first service:\n'))
s_service = str(input('Select second service:\n'))
print('')

# 3 and 4. Output an invoice for the services selected. Output the cost for each service and the total cost.
print("Davy's auto shop invoice")
print('')

if f_service == '-':
    print('Service 1: No service')
    print('Service 2: ', s_service, ', $', services.get(s_service), sep='')
    print('')
    total = services.get(s_service)
    print('Total: $', total, sep='')
elif s_service == '-':
    print('Service 1: ', f_service, ', $', services.get(f_service), sep='')
    print('Service 2: No service')
    print('')
    total = services.get(f_service)
    print('Total: $', total, sep='')
else:
    print('Service 1: ', f_service, ', $', services.get(f_service), sep='')
    print('Service 2: ', s_service, ', $', services.get(s_service), sep='')
    print('')
    total = services.get(f_service) + services.get(s_service)
    print('Total: $', total, sep='')





