# make some noise if the hour provided (in terminal) is not equal with current hor from US/EASTERN timezone

import winsound
import time
from datetime import datetime
#install this library, running in terminal: pip install pytz
import pytz

def play_sound():
    i = 0
    while i < 5:
        i = i + 1
        winsound.PlaySound("*", winsound.SND_ALIAS)
        time.sleep(1)


tz = pytz.timezone("US/Eastern")
today = datetime.now(tz)

print('What is the time in Washington, D.C.: ')
x = input()
if int(x) == today.hour:
    play_sound()
    print(today)
else:
    print('Bad luck! The correct date and time: ', today)