import pyautogui
from time import sleep
import keyboard
import win32api
import win32con

pyautogui.click(1013,385,duration=2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(913,348,(0,0,0)):
       click(913,348) 
    if pyautogui.pixelMatchesColor(985,351,(0,0,0)):
       click(985,351) 
    if pyautogui.pixelMatchesColor(1048,363,(0,0,0)):
       click(1048,363) 
    if pyautogui.pixelMatchesColor(1127,341,(0,0,0)):
       click(1127,341) 
    
    
