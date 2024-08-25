#crie um programaque vá até onde seu bloco de notas esta aberto e digite"A automação é incrivel"

#importar biblioteca
import pyautogui
import pyperclip
# Criar uma função
def mensagem(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')
# Achar o local no blocos de notas,Clicar para abrir
pyautogui.click(1021,118,duration=2)
# Escrever a mensagem
mensagem('A automação é incrível!')