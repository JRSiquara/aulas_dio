# Manipulando arquivos externos.
# arquivo = open('teste.txt', 'w')  # 'w' sobre-escreve
# arquivo.write('Minha primeira escrita')
# arquivo = open('teste.txt', 'a')    # 'a' adiciona, utilizando \n como "enter"
# arquivo.write('\nMinha segunda escrita')
# arquivo.close()

import shutil
def escrever_arquivo(texto):
    diretorio = 'D:/Drago/DIO-CURSOS-EAD/PYTHON/projetos/teste.txt' # No Python usar barra '/'
    arquivo = open(diretorio, 'w')  # 'w' write (escreve)
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')  # 'a' adiciona
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')  # 'r' read (ler)
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') # split() le a linha até encontrar '\n' "Enter"
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_nota = x.split(',')  # split() le a linha até encontrar ',' "Enter"
        aluno = lista_nota[0]
        lista_nota.pop(0)
        print(aluno)
        print(lista_nota)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_nota))
        lista_media.append({aluno:media(lista_nota)})
    return lista_media

def copia_arquivo(nome_arquivo):
    # import shutil # O melhor é colocar este comando no inicio do método (programa/arquivo.py)
    shutil.copy(nome_arquivo, 'D:/Drago/DIO-CURSOS-EAD/notas_alunos.txt')

def move_arquivo(nome_arquivo):
    #shutil.move(nome_arquivo, 'D:/Drago/DIO-CURSOS-EAD/')
    pass

if __name__ == '__main__':
    #move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira linha.\n')
    aluno = 'Cesar,7,9,3,8\n'
    atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')

