# digitar com pyautogui

import pyautogui
import pyperclip
def escrever_mensagem(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.moveTo(1114,517,duration=2)
pyautogui.click()
escrever_mensagem('Olá, bom diaaa')
pyautogui.click(1253,520,duration=2)