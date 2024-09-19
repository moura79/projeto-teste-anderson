import pyautogui
from time import sleep
import keyboard 
while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(916,548,(0,152,0)):
        pyautogui.press('a')
        sleep(0.04)
    if pyautogui.pixelMatchesColor(971,568,(255,0,0)):
        pyautogui.press('s')
        sleep(0.04)
    if pyautogui.pixelMatchesColor(1068,569,(244,244,2)):
        pyautogui.press('j')
        sleep(0.04)