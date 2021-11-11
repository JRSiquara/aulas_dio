conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

print('conjunto1: {con}'.format(con=conjunto1))
print('conjunto2: {con2}'.format(con2=conjunto2))

conjunto_uniao = conjunto1.union(conjunto2)
print('União dos conjuntos: {conuni}'.format(conuni=conjunto_uniao))

conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Interseção dos conjuntos: {conint}'.format(conint=conjunto_interseccao))

conjunto_dif1 = conjunto1.difference(conjunto2)
print('Diferença conjunto1 x conjunto2: {}'.format(conjunto_dif1))

conjunto_dif2 = conjunto2.difference(conjunto1)
print('Diferença conjunto2 x conjunto1: {}'.format(conjunto_dif2))

conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
print('Conj. A: {}'.format(conjunto_a),' Conj. B: {}'.format(conjunto_b))
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é Subconjunto(está contido) de B (True/False) ? {}'.format(conjunto_subset))

conjunto_subset = conjunto_b.issubset(conjunto_a)
print('B é Subconjunto(está contido) de A (True/False) ? {}'.format(conjunto_subset))

conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('A é Conjunto(contém) de B (True/False) ? {}'.format(conjunto_superset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é Conjunto(contém) de A (True/False) ? {}'.format(conjunto_superset))

# set() converte lista para conjunto
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print('Lista com animais: {}'.format(lista),'Type lista: {}'.format(type(lista)))
print('***** Convertendo Lista para Conjunto *****')
conjunto_animais = set(lista)
print('Conjunto com animais: {}'.format(conjunto_animais),'Type conjunto: {}'.format(type(conjunto_animais)))

# list() converte conjunto para lista
print('***** Convertendo Conjunto para Lista *****')
lista_animais = list(conjunto_animais)
print('Nova lista com animais: {}'.format(lista_animais),'Type Nova lista: {}'.format(type(lista_animais)))


# conjunto = {1, 2, 3, 4, 2, 3, 3}
# print(type(conjunto))
# print(conjunto)
# print(len(conjunto))
# conjunto.add(3)
# print(conjunto)
# conjunto.discard(2)
# print(conjunto)