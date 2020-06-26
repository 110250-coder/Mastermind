import random
from random import randint





print(' ')
print("Beste speler welkom bij mastermind!")
print(' ')
print("Bij dit spel kiest de computer 4 van de 6 kleuren (Rood, Blauw, Groen, Citroengeel, Paars, Magenta) en jij moet raden welke 4 kleuren er gekozen zijn en op welke volgorde ze staan. Je krijgt 10 beurten, bij elke beurt kies je de voorste letter van een kleur naar keuze (een kleur kan meerdere keren gebruikt worden) en in een volgorde naar keuze. Als je alles goed hebt heb je gewonnen. Zo niet krijg je hints het aantal “Z’s” (van Zwart) geeft aan dat er een gekozen kleur in de code voorkomt en op de juiste positie staat. Het aantal “W’s” (van Wit) geeft het aantal keer dat een kleur voorkomt, maar die niet op de juiste positie staan aan.")
print(' ')
print(' ')
print(' ')


kleuren = ['r', 'b', 'g', 'c', 'p', 'm']

volgorde = random.sample(kleuren,4)

tries = 0
loop = True

while loop:
  goedekleur = ''
  kleurpoging = ''
  poging = input('').lower()
  tries = tries + 1

  if len(poging) != 4 :
    print(' ')
    print('De code heeft 4 letters nodig! Probeer opnieuw!')
    print(' ')
    continue
  if goedekleur != 'zzzz' :
    for i in range(4):
      if poging[i] == volgorde[i]:
       goedekleur += 'z'
      if poging[i] != volgorde[i] and poging[i] in volgorde :
       kleurpoging += 'w'
    print(goedekleur + kleurpoging)
    if 10 - tries == 1 :
      print(' ')
      print('Je hebt nog 1 kans om de code te raden')
      print(' ')
      continue
    elif  10 - tries == 0 :
      print(' ')
      print('Game over')
      print('Helaas je hebt het niet geraden')
      break
    else :
      print(' ')
      print('Je hebt nog ' + str(10 - tries) + ' kansen om de code te raden!')
      print(' ')
      continue
  for i in range(4):
   if poging[i] not in kleuren :
      print(' ')
      print('Je kan alleen de kleuren Paars, Blauw, Groen, Magenta, Rood en Citroengeel gebruiken! Probeer opniew!')
      print(' ')
      break
