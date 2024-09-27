""" PASSOS PARA AUTOMATIZAR
1 - ESCOLHER CONTATO
2 - ENVIAR MENSAGEM PARA ESSE CONTATO
	https://api.whatsapp.com/send?phone=5511945051719
3 - reptir para outros contatos """

import pyautogui
from time import sleep
import webbrowser

telefones = [5511945051719,5511993632740,5512988365721]
for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(438,611,duration=1)
    sleep(5)
    pyautogui.typewrite('boa tarde!')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)