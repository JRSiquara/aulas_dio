
lista = [1, 10]
try: # Tudo que estiver no "try" entra no tratamento de exceção.
    arquivo = open('teste.txt', 'r')
    divisao = 10 / 1
    numero = lista[1]
    x = a
except ZeroDivisionError: # ZeroDivisionError - É uma classe de exceções que tem built in no Phyton.
    print('Não é possível realizar uma divisão por zero (0).')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimética.')
except IndexError: # Posso colocar a classe IndexError: ou não colocar nada p/ tratar todas como erro desconhecido.
    print('Erro ao acessar um índice fora da lista. ')
except Exception as ex: # Exception (filho da BaseException, mas pai de todas as outras).
    print('Erro desconhecido: "{}'.format(ex)+'" - Da classe: '+str(NameError))
except BaseException as ex: # BaseException é o pai de todas as exceções. Aqui utilizando o "as" está
                            # gravando a mensagem de erro no "ex".
    print('Erro desconhecido. Verifique os erros nas classes (SystemExit,'+
          ' KeyboardInterrupt, GeneratorExit): {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally: # Aqui sempre executa os comandos.
    print('Sempre executa ocorrendo ou não exceção.')
    print('Fechando arquivo no finally')
    arquivo.close()