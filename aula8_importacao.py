from aula7_televisao import Televisao  # Importando a Classe Televisao do módulo aula7_televisao.py
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras, teste  # Pode importar mais de função, Classe e etc.

if __name__ == '__main__':
    televisao = Televisao()  # Instanciando
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)  # Instanciando
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Palavras: {}'.format(lista))
    print('Total de letras por palavras: {}'.format(total_letras))
    print(teste())

