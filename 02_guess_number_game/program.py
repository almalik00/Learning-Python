import random

print('--------------------------------')
print('     GUESS NUMBER GAME')
print('--------------------------------')

the_number = random.randint(0, 100)

guss = -1

name = input('(Player) what is your name: ')
while guss != the_number:
    guss_text = input('Guss a number between 0 and 100:  ')
    guss = int(guss_text)

    if guss < the_number:
        print('Sorry {1}, your guss of {0} was too low, '.format(guss, name))
    elif guss > the_number:
        print('Sorry {1}, your guss of {0} was too high, '.format(guss, name))
    else:
        print('Hora {1},  you win!'.format(guss, name))

print('done thank you ')

