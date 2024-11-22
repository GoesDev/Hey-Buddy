from time import sleep
from datetime import datetime
# from db_functions import save_task
import os
os.system('cls')

# DICIONÁRIO COM OS VALORES PADRÕES DOS CONTADORES
# PODE SER ALTERADO PELA FUNÇÃO update_counter()
counter_standard_minutes = {
    "pomodoro": 25,
    "short_rest": 5,
    "long_rest": 15
}

# DICIONÁRIO DA ATIVIDADE
task = {
    "Category": "Chess",
    "Name": "2x Chess Games",
    "Date": "",
    "Start_Time": "",
    "End_Time": "",
    "Minutes": ""
}


def update_counter(counter_type: str, minutes: int):
    """
    Função que atualiza os valores padrões dos Contadores

        Args
        counter_type (str): informa a chave do dict
        counter_standard_minutes que será atualizada

        minutes (int): o novo valor em minutos que a chave terá

    """

    counter_standard_minutes[counter_type] = minutes


def end_counter(start_counter_time):
    """
    Função que registra no dicionário da atividade atual
    a hora de finalização do contador

    Return:
        end_counter_time (): retorna a hora de finalização da atividade
    """

    end_counter_time = datetime.now()
    task["End_Time"] = end_counter_time.strftime("%H:%M")
    time_difference = end_counter_time - start_counter_time
    minutes = int(time_difference.total_seconds() / 60)
    task['Minutes'] = minutes
    print(task)


def start_counter():
    """
    Função que inicia a contagem do Contador

        Args counter_type (str): informa a chave do dict
        counter_standard_minutes e pega o valor da contagem
    """
    start_counter_time = datetime.now()
    task["Date"] = start_counter_time.strftime("%d/%m/%Y")
    task["Start_Time"] = start_counter_time.strftime("%H:%M")

    return start_counter_time


def counter(counter_type):

    start_counter_time = start_counter()

    seconds = counter_standard_minutes[counter_type] * 60

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")
        sleep(1)
        seconds -= 1
        if seconds == 0:
            end_counter(start_counter_time)


update_counter("short_rest", 1)
counter("short_rest")
