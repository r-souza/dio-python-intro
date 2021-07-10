grade = int(input('Enter a grade: '))

while grade > 10:
    grade = int(input('Invalid grade, enter a grade less than or equal to 10: '))

print('Grade entered: {}'.format(grade))
