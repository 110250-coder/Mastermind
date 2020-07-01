import random
import colorama
from colorama import Fore,Style
#
# While loop voor Eindespel
#
while True :

#
# Introductie
#
  print(' ')
  print('Beste speler welkom bij mastermind!')
  print(' ')
  print('Bij dit spel kiest de computer 4 van de 6 kleuren (Rood, Blauw, Groen, Citroengeel, Paars, Magenta) en jij moet raden welke 4 kleuren er gekozen zijn en op welke volgorde ze staan.\n\nJe krijgt 10 beurten, bij elke beurt kies je de voorste letter van een kleur naar keuze (een kleur kan meerdere keren gebruikt worden) en in een volgorde naar keuze. Als je alles goed hebt heb je gewonnen.\n\nZo niet krijg je hints het aantal “Z’s" (van Zwart) geeft aan dat er een gekozen kleur in de code voorkomt en op de juiste positie staat. Het aantal “W’s” (van Wit) geeft het aantal keer dat een kleur voorkomt, maar die niet op de juiste positie staan aan.')
  print(' ')
  print(' ')
  print(' ')
  #
  # Functie ophogen van tries
  #
  def ophogen():
    global tries 
    tries = tries + 1
#
# definitie van alle variabelen
#
  kleuren = ['r', 'b', 'g', 'c', 'p', 'm']
  volgorde = random.sample(kleuren,4)
  tries = 0
  loop = True
#
# While loop zolang we het spel spelen
#
  while loop: # zolang loop is true
    goedekleur = ''
    kleurpoging = ''
    poging = input('').lower()
#
# Functie ophogen aanroepen om tries met 1 op te hogen
#
    ophogen()
#
# Concatenation    
#
    a = 'Je hebt nog ' 
    b = ' kansen om de code te raden!'
    c = ' kans om de code te raden!'
    d = a + str(10 - tries) + b
    e = a + str(10 - tries) + c
#
# als poging niet gelijk 4 of bevat nummers
#
    if len(poging) != 4 or not poging.isalpha():
      print(' ')
      print(Fore.RED +'De code heeft 4 letters nodig en mag geen cijfers bevatten!\n\n Probeer opnieuw!')
      print(Style.RESET_ALL)
      print(' ')
#
# Aantal resterende pogingen berekenen bij foute invoer
#
      if 10 - tries == 1 :
        print(' ')
        print(e) #concatenation
        print(' ')
        continue
      elif  10 - tries == 0 :
        print(' ')
        print('Helaas je hebt het niet geraden')
        print(' ')
        break
      else :
        print(' ')
        print(d) #concatenation
        print(' ')
        continue
#
# zitten de juiste kleuren erin
#
    for i in range(4):
      if poging[i] not in kleuren :
        print(' ')
        print('Je mag alleen de kleuren Paars, Blauw, Groen, Magenta, Rood en Citroengeel gebruiken! Probeer opnieuw!')
        print(' ')
        break
#
# Goed en/of goede plaats bepalen
#
    if goedekleur != 'zzzz' :
      for i in range(4):
        if poging[i] == volgorde[i]:
          goedekleur += 'z'
        if poging[i] != volgorde[i] and poging[i] in    volgorde :
         kleurpoging += 'w'
      print(goedekleur + kleurpoging)
# Alle kleuren goed!      
      if goedekleur == 'zzzz' : 
       print('GEFELICITEERD je hebt het geraden!')
       break # ga uit de while loop om naar eindespel te gaan
#
# Aantal resterende pogingen berekenen bij juiste invoer
#
      if 10 - tries == 1 :
        print(' ')
        print(e) #concatenation
        print(' ')
        continue
      elif  10 - tries == 0 :
        print(' ')
        print('Game over')
        print('Helaas je hebt het niet geraden')
        break
      else :
        print(' ')
        print(d) #concatenation
        print(' ')
        continue
#
# Zullen we nog een keertje spelen?
#
  eindespel = input('Wil je het nog een keer proberen (j/n)').lower()
  if eindespel == 'n':
    print(' ')
    print ('Bedankt voor het spelen. Tot ziens!')
    print(' ')
    break # ga uit de while true loop
  else :
    print(' ')
    print ('Laten we nog een keer spelen')
    print(' ')
    continue # blijf binnen de while true loop en speel opnieuw
    
