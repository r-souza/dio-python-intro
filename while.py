note = int(input('Enter a note: '))

while note > 10:
    note = int(input('Invalid note, enter a nota below or equal to 10: '))

print('Note entered: {}'.format(note))
