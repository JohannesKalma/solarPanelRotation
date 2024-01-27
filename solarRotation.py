from datetime import datetime
import time
import sys

# deze waardes ophalen van een api service (zoals weerlive[knmi] of openweathermap)
time_sunrise = "07:54".split(":")
time_sunset = "17:15".split(":")

# epoch waardes (secondes sinds 1-1-1970) berekenen voor zonsopkomst, zonsondergang, 
# sommige api's doen dat overigens als, hoef je het hier niet nog een keer te doen natuurlijk
today = datetime.today();
sunrise = int(today.replace(hour=int(time_sunrise[0]), minute=int(time_sunrise[1]),second=0, microsecond=0).strftime('%s'));
sunset = int(today.replace(hour=int(time_sunset[0]), minute=int(time_sunset[1]),second=0, microsecond=0).strftime('%s'));
# hoe lang (in secondes) is de zon vandaag boven de horizon
sunAboveHorizonToday = (sunset-sunrise);
#### print(f'De zon schrijnt vandaang {sunupToday} seconden')

# bepaal iedere 10 seconden de huidige stand van de zon tov het oosten (sunrise)
# aanname: de zon komt op in het oosten (90 graden) en gaat onder in het westen (270 graden)
# wil je exacter werken, dan moet je de azimut waardes berekenen obv de lokatie
# https://nl.wikipedia.org/wiki/Azimut
# vraag maar aan chatgpt of bard
# voor nu is de sunupToday gelijk aan 180 graden.
# sunupToday (seconden) = 180 graden
# berekening is:
# de hele dag dat de zon op is (dat is de sunupToda, dus tussen opkomst en ondergang is 180 graden.
# de dag is dus in 'secondegraden' op te delen door 180/(seconden dat de zon op is vandaag) 
# bereken nu we de tijd tussen de zonsopkomst en nu in seconden
# als je dan die 2 waarden vermenigvuldigt, heb je aantal graden dat de zon is verschoven tov punt waar deze op kwam (het oosten)
bewaarGraden = None
while True:
    now = datetime.now()
    nows = int(now.strftime('%s'));
    nowf = now.strftime("%-d-%m-%Y %-H:%M:%S")
    sunupSinceSunrise = nows-sunrise
    gradenNu = (nows-sunrise)*(180/sunAboveHorizonToday)
    afgerondeGradenNu=round(gradenNu)
    if bewaarGraden != afgerondeGradenNu :
      bewaarGraden = afgerondeGradenNu
      sys.stdout.write('\r')
      print(f'Het is nu {nowf} en de zon schijnt al {sunupSinceSunrise} seconden en is {afgerondeGradenNu} graden gedraaid tov het oosten')
    else :
      sys.stdout.write('.')
      sys.stdout.flush()
    time.sleep(5);
    