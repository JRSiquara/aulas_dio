# A função date() é do módulo datetime, assim como a função datetime().
from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    print(type(data_atual)) # <class 'datetime.date'>
    print(data_atual.strftime('%d/%m/%Y')) # %y 2 digitos (21), o %Y 4 digitos (2021).
    print(data_atual.strftime('%A %B %Y')) # Wednesday November 2021
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual_str)) # <class 'str'>

# Este link mostra exibe (diretiva) lista com todos os códigos de formatação srtftime() e strptime()
# https://docs.python.org/pt-br/3/library/datetime.html?highlight=datetime#module-datetime

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(type(horario))  # <class 'datetime.time'>
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario_str)) # <class 'datetime.time'>
    print(horario_str)

def trabalhando_com_datetime():
    data_atual = datetime.now() # Para ser usadas todas as funções precisam ser declaradas no
                                # (from <modulo> import).
    print(type(data_atual))
    print(data_atual) # "2021-11-03 14:08:31.231779"
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S')) # Format e retira os milisegundos "03/11/2021 14:08:31"
    print(data_atual.strftime('%c')) # "Wed Nov  3 14:11:23 2021"
    print(data_atual.day) # Só o dia.
    print(data_atual.month) # Só o mês.
    print(data_atual.year) # Só o year.
    print(data_atual.hour) # Só o hora.
    print(data_atual.date()) # Só o data.
    print(data_atual.weekday()) # Só o dia da semana.

    # Esta tupla permite mostrar o dia da semana em português, onde 'Segunda" = 0 e 'Domingo' = 6
    tupla = ('Segunda', 'terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(type(tupla)) # "<class 'tuple'>"
    print(tupla[data_atual.weekday()]) # "Quarta"

    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada) # "2018-06-20 15:30:20"
    print(data_criada.strftime('%c')) # "Wed Jun 20 15:30:20 2018"

    # Permite converter uma data em string para data com o strptime().
    data_string = '01/01/2019 12:20:22'
    print(type(data_string)) # <class 'str'>
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(type(data_convertida)) # <class 'datetime.datetime'>
    print(data_convertida) # 2019-01-01 12:20:22

    # Usando a função timedelta() para operações com datas e horas.
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print('Data convertida: {} '.format(data_convertida))  # "Data convertida: 2019-01-01 12:20:22"
    print('Data nova_data: {} '.format(nova_data))         # "Data nova_data: 2018-01-01 10:05:22"


if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime() # Dica: Posicionando o curso na função e pressionar ctrl+"clique do mouse" vai
                               # direto para def função ou classe ou metodo.
