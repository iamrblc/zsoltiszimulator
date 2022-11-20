'''
This is a simple leaping frog simulator. It either jumps left or right randomly as many times as you want.
At the end we'll see how many times it got back to the original position and how far it could hop.   

Ez egy egyszerű Zsolti, a béka szimulátor. Vagy jobbra vagy balra ugrik véletlenszerűen annyiszor, ahányszor csak szeretnéd.
A végén meglátjuk, hogy ezalatt hányszor szökellt vissza a kiinduló helyére és hogy meddig jutott.
'''

import random

ugrasmennyiseg = int(input("How many times should the frog leap? "))
zsolti_pozi = 0
visszateres = 0

def ugribugri():
    merre = bool(random.getrandbits(1))
    if merre == True:
        return zsolti_pozi + 1
    else:
        return zsolti_pozi - 1

i = 0
legbalrabb = 0
legjobbrabb = 0
while i < ugrasmennyiseg:
    zsolti_pozi = ugribugri()
    if zsolti_pozi == 0:
        visszateres = visszateres + 1
    if zsolti_pozi < legbalrabb:
        legbalrabb = zsolti_pozi
    elif zsolti_pozi > legjobbrabb:
        legjobbrabb = zsolti_pozi

    i += 1

print("Szegény Zsoltit " + str(ugrasmennyiseg) + " alkalommal ugráltattad. Ezalatt " + str(visszateres) + " alkalommal szökkent vissza a kiindulási helyére.")
print("Balra legmesszebb " + str(abs(legbalrabb))+ ", jobbra pedig " + str(legjobbrabb) + " ugrásnyira jutott.")

print("You made poor frog jump " + str(ugrasmennyiseg) + " times. Meanwhile he leaped back to the start position " + str(visszateres) + " times.")
print("He reached the furthest " + str(abs(legbalrabb))+ " jumps to the left and " + str(legjobbrabb) + " to the right.")