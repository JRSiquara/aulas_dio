class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self): # Definação de um método. É um método que tem uma função de retornar a soma.
        return self.valor_a + self.valor_b

    def subtracao(self): # É um método que tem uma função de retornar a subtração.
        return self.valor_a - self.valor_b

    def multiplicacao(self): # É um método que tem uma função de retornar a Multiplicação.
        return self.valor_a * self.valor_b

    def divisao(self): # É um método que tem uma função de retornar a Divisão.
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(10, 2)    #Isso é instanciar.

    print(calculadora.valor_a)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.divisao())
    print(calculadora.multiplicacao())



# print(soma(3, 4))
# print(subtracao(20, 10))
# print(multiplicacao(3,5))
# print(divisao(10, 2))
