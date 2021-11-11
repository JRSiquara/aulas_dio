# def contador_letras(lista_palavras):
#
#     contador = [] # [] Colchetes cria lista.
#     for x in lista_palavras:
#         quantidade = len(x)
#         contador.append(quantidade)
#     return contador
# A função lambda permite otimizar códigos. O exemplo acima será reescrito usando apenas 1 linha usando lambda.

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(10, 5))
print(subtracao(10, 5))

# Dicionário
calculadora = {
    'soma': lambda a, b: a + b,
    'sbutracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}
print(type(calculadora))
soma = calculadora['soma']  # soma = lambda a, b: a + b
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(multiplicacao(10, 2)))

