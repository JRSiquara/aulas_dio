class Calculadora:
#    def __init__(self): Aqui como valores serão passados direto no método, ñ precissa iniciar.
#        pass   # O __init__() não pode ficar vazio, o "pass" não faz nada.

    def soma(self, valor_a, valor_b): # Definação de um método. É um método que tem uma função de retornar a soma.
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b): # É um método que tem uma função de retornar a subtração.
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b): # É um método que tem uma função de retornar a Multiplicação.
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b): # É um método que tem uma função de retornar a Divisão.
        return valor_a / valor_b

calculadora = Calculadora()    #Isso é instanciar.

print(calculadora.soma(10, 2))
print(calculadora.subtracao(10, 2))
print(calculadora.divisao(10, 2))
print(calculadora.multiplicacao(10, 2))