from time import sleep
from datetime import datetime

# DICIONÁRIO COM OS VALORES PADRÕES DOS CONTADORES
# PODE SER ALTERADO PELA FUNÇÃO update_counter()
counter_standard_minutes = {
    "pomodoro": 25,
    "short_rest": 5,
    "long_rest": 15
}

# DICIONÁRIO DA ATIVIDADE
activity = {
    "name": "2x Chess Games",
    "category": "Chess",
    "difficulty": "Easy"
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


def end_counter():
    """
    Função que registra no dicionário da atividade atual
    a hora de finalização do contador
    """

    end_counter_time = datetime.now()
    activity["end_time"] = end_counter_time.strftime("%H:%M")


def start_counter(counter_type: str):
    """
    Função que inicia a contagem do Contador

        Args counter_type (str): informa a chave do dict
        counter_standard_minutes e pega o valor da contagem
    """

    start_counter_time = datetime.now()
    activity["date"] = start_counter_time.strftime("%d/%m/%Y")
    activity["start_time"] = start_counter_time.strftime("%H:%M")

    seconds = counter_standard_minutes[counter_type] * 60

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")
        sleep(1)
        seconds -= 1
        if seconds == 0:
            end_counter()


# update_counter("short_rest", 3)
start_counter("short_rest")

for key, value in activity.items():
    print(f"{key.title()}: {value}")
