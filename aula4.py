a = int(input('Entre com o 1º bimenstre: '))
while a > 10:
    a = int(input('Digitou errado. Entre com o 1º bimenstre: '))
b = int(input('Entre com o 2º bimenstre: '))
while b > 10:
    b = int(input('Digitou errado. Entre com o 2º bimenstre: '))
c = int(input('Entre com o 3º bimenstre: '))
while c > 10:
    c = int(input('Digitou errado. Entre com o 3º bimenstre: '))
d = int(input('Entre com o 4º bimenstre: '))
while d > 10:
    d = int(input('Digitou errado. Entre com o 4º bimenstre: '))
media = (a + b + c + d) / 4
print('Média : {m}'.format(m=media))

# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota: '))
# print(nota)

# a = 0
# while a <= 10:
#     print(a)
#     a += 4

# a = int(input('Entre com o Nº: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             #div = div + 1
#             div += 1
#     if div == 2:
#         print(num)

# a = int(input('Entre com o Nº: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         #div = div + 1
#         div += 1
# if div == 2:
#     print('Nº é primo: {}'.format(a))
# else:
#     print('Nº não é primo: {}'.format(a))
