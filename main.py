import random
from random import randint





print(' ')
print("Beste speler welkom bij mastermind!")
print(' ')
print("Bij dit spel kiest de computer 4 van de 6 kleuren (Rood, Blauw, Groen, Citroengeel, Paars, Magenta) en jij moet raden welke 4 kleuren er gekozen zijn en op welke volgorde ze staan. Je krijgt 10 beurten bij elke beurt kies je de voorste letter van een kleur naar keuze (een kleur kan meerdere keren gebruikt worden) in een volgorde naar keuze. Als je alles goed hebt heb je gewonnen. Zo niet krijg je hints het aantal “Z’s” (van Zwart) geeft aan dat er een gekozen kleur in de code voorkomt en op de juiste positie staat. Het aantal “W’s” (van Wit) geeft het aantal keer dat een kleur voorkomt, maar die niet op de juiste positie staan aan.")
print(' ')
print(' ')
print(' ')


kleuren = ['r', 'b', 'g', 'c', 'p', 'm']

volgorde = random.sample(kleuren,4)

tries = 0
loop = True

while loop:
  poging = input('')
  tries = tries + 1

  if len(poging) != 4 :
    print('De code heeft 4 letters nodig! Probeer opnieuw!')
    print(' ')
    print('Je hebt nog ' + str(10 - tries) + ' kansen om de code te raden!')
    continue