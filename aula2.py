a = int(input('Entre com o 1º valor: '))
b = int(input('Entre com o 2º valor: '))
soma = a + b
subtrac = a - b
mult = a * b
div = a / b
resto = a % b
resultado = ('soma: {som}'
      '\nSubtração: {subt}' 
      '\nMultiplicação: {mu}' 
      '\nDivisão: {di}' 
      '\nResto: {res}'.format(som=soma,
                                subt=subtrac,
                                mu=mult,
                                di=div,
                                res=resto))
print(resultado)
      # '\nSubtração: {subtrac}'
      # '\nMultiplicação: {mult}'
      # '\nDivisão: [div}'
      # '\nResto: {resto}'.format(soma=soma, subtrac=subtrac,
      #                                           mult=mult,
      #                                           div=div,
      #                                           resto=resto))
# print('Inteiro: ' + str(int(div)))
# print(div)
# print(resto)
# x = '1'
# soma2 = int(x) + 1
# print(soma2)