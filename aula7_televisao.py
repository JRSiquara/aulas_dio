#  Ctrl+F8 ativa e dasativa parada na linha.
#  Shift+F9 roda debug
#  F8 linha a linha
class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):  # Exemplo de método que não retorna, apenas tranforma o valor
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

# print(__name__)
if __name__ == '__main__': # Na importação do módulo, evita executar as linhas de dentro do if.
    televisao = Televisao()  # instanciar
    televisao.power()
    print('Tv está ligada ? {}'.format(televisao.ligada))
    televisao.power()
    print('Tv está ligada ? {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Tv está ligada ? {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal {} '.format(televisao.canal))
