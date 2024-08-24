import pyautogui
from time import sleep
#Posição de algo - use o mouseInfo
#Fazer algo com essa posição
pyautogui.moveTo(994,254,duration=1.5)
for i in range(500):
    sleep(0.1)
    pyautogui.click()