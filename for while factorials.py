#forfact.py
n = int(input('Enter an integer >= 0: '))
fact = 1
for i in range(2,n+1):
    fact = fact * i
print(str(n)+ ' factorial is ' + str(fact))

#whilefact.py
n = int(input('Enter an integer >=0: '))
fact = 1
i = 2
while i<=n:
    fact = fact*i
    i = i+1
print(str(n) + ' factorial is ' + str(fact))

#forsum.py
n = int(input('How many numbers to sum? '))
total = 0
for i in range(n):
    s = input('Enter number ' + str(i+1) + ': ')
    total = total + int(s)
print('The sum is ' + str(total))

#whilesum.py
n = int(input('How many numbers to sum? '))
total = 0
i = 1
while i<=n:
    s = input('Enter number ' + str(i) + ': ')
    total = total+int(s)
    i = i + 1
print('The sum is ' + str(total))

#just while, summing unknown number of numbers
#donesum.py
total = 0
s = input('Enter a number(or "done"): ')
while s != 'done':
    num = int(s)
    total = total + num
    s = input('Enter a number (or "done"): ')
print('The sum is ' + str(total))

#donesum_break.py
total = 0
while True:
    s = input('Enter a number (or "done"): ')
    if s=='done':
        break # jump out of loop
    num = int(s)
    total = total + num
print('The sum is ' + str(total))

#nested loops
#timestable.py times tables up to 10
for row in range(1,10):
    for col in range(1,10):
        prod = row*col
        if prod < 10:
            print(' ', end='')
        print(row*col, ' ', end='')
    print()
