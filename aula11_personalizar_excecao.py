class Error(Exception):  # Classe de exceção personalizada. É obrigação ter sempre essas
    pass                 # duas classes "Error e InputError".

class InputError(Error):  # Por convenção toda classe deve terminar com "Error".
    def __init__(self, message): # Criando um construtor (Ver na aula de classes).
        self.message = message

while True:
    try:
        x = int(input('Entre com nota (0 a 10): '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10.') # comando raise força uma exceção.
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break  # Força a saida do while.
    except ValueError:
        print('Valor inválido: Digitar apenas números')
    except InputError as ex:
        print(ex)