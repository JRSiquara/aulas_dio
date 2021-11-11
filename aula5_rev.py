lista = [1, 3, 7, 5]
#var = ['cachorro', 'gato', 'elefante']

# Código que modifica uma coleção sobre a qual está iterando pode ser inseguro.
# No lugar disso, usualmente você deve iterar sobre uma cópia da coleção ou criar uma nova coleção:

#print(lista_animal)
#print(len(lista_animal)-1)
#tam = len(lista_animal)-1
#print(type(tam))

# As listas vão sendo modificadas conforme a interação com elas. Ver no debug (ctrl+F8)

def lista_esvaziando_traz_frente():
    lista_animal = ['cachorro', 'gato', 'elefante']
    print(str.upper('"lista_esvaziando_traz_frente()"'))
    lista_esvaziando = lista_animal
    for x in lista_animal:
        #print('x: {}'.format(x))
        print('Lista_esvaziando: {}'.format(lista_esvaziando))
        lista_animal.pop()  # Retira o ultimo
        lista_esvaziando = lista_animal

    #print('x: {}'.format(x))
    print('Lista_esvaziando: {}'.format(lista_esvaziando))

def lista_esvaziando_frente_traz():
    lista_animal = ['cachorro', 'gato', 'elefante']
    print(str.upper('"lista_esvaziando_frente_traz()"'))
    for x in lista_animal:
        #print('x: {}'.format(x))
        print('Lista_esvaziando: {}'.format(lista_animal))
        lista_animal.pop(0)  # Retira o primeiro

    #print('x: {}'.format(x))
    print('Lista_esvaziando: {}'.format(lista_animal))

# Neste exemplo utilizei a tupla por não permitir alteraçao da cadeia de string.
# diferente do que ocorre co a lista.

def lista_esvaziando_frente_traz_tupla():
    lista_animal = ['cachorro', 'gato', 'elefante']
    lista_esvaziando = tuple(lista_animal)
    print(str.upper('"lista_esvaziando_frente_traz_tupla()"'))

    for x in range(len(lista_esvaziando)):
        #print('x: {}'.format(x))
        print('Lista_esvaziando: {}'.format(lista_animal))
        lista_animal.pop(0)  # Retira o primeiro

if __name__ == '__main__':
    lista_esvaziando_traz_frente()
    lista_esvaziando_frente_traz()
    lista_esvaziando_frente_traz_tupla()

# for x in :
#     print(lista_animal)
#     lista_animal.pop(x)

