#airfare.py
age = int(input('How old are you? '))
if age<=2:
    print('free')
elif 2<age<13:
    print('child fare')
else:
    print('adult fare')

