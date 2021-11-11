lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla =  (1, 10, 12, 14)
print(tupla)
print(len(tupla))
print(len(lista_animal))

tupla_animal = tuple(lista_animal) # Converte lista em tupla
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla) # Converte tupla em lista
print(type(lista_numerica))
print(lista_numerica)
lista_numerica[0] = 333
print(lista_numerica)

#nova_lista = lista_animal * 3
#print(nova_lista)

# print(lista)
# lista.sort()
# print(lista)
# print(lista_animal)
# lista_animal.sort()
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# if 'lobo' in lista_animal:
#     print('Existe lobo na lista')
# else:
#     print('Não existe lobo na lista. Será incluido.')
#     lista_animal.append('lobo') # append inclui
#     print(lista_animal)

#lista_animal.pop(0)  # pop() retira o ultimo elemento da lista
#print(lista_animal) # pop(0) retira na posição o elemento da lista


# print(sum(lista))
# print(max(lista))
# print(min(lista))

# print(lista[3])
# print(lista_animal[1])
#
# for x in lista_animal:
#     print(x)