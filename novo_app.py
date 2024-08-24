from time import sleep
def calcular_preco_combo(pizza,refrigerante):
    total = pizza + refrigerante
    print('Calculando...')
    sleep(0.8)
    print('O total deu R$',total)
calcular_preco_combo(50,21)
print('Programa final')