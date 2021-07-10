a = int(input('Please enter a number: '))

div = 0

for x in range(1, a+1):
    mod = a % x
    if mod == 0:
        div += 1

if div == 2:
    print('Number {} is a prime'.format(a))
else:
    print('number {} is not prime'.format(a))
