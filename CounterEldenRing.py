import pyautogui
from time import sleep
import os
clear = lambda: os.system('cls')



res = pyautogui.locateOnScreen("./img/VousAvezPeri.png", confidence=0.5, region=(580,460,770,170))
count = 0

while (count != 100000):
    while (res == None):
        res = pyautogui.locateOnScreen("./img/VousAvezPeri.png", confidence=0.5, region=(580,460,770,170))
        sleep(0.1)   
    else:
        res = pyautogui.locateOnScreen("./img/VousAvezPeri.png", confidence=0.5, region=(580,460,770,170))
        clear()
        count = count + 1
        print("Tu es mort %i fois" % count) 
        
        
        res = None
        sleep(15)
        