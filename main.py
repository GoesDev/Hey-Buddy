from time import sleep
from datetime import datetime
from db_functions import save_category, select_all_categories
import os
os.system('cls')

# DICIONÁRIO COM OS VALORES PADRÕES DOS CONTADORES
# PODE SER ALTERADO PELA FUNÇÃO update_counter()
counter_standard_minutes = {
    "Pomodoro": 25,
    "Short_Rest": 5,
    "Long_Rest": 15
}

# DICIONÁRIO DA ATIVIDADE
task = {
    "Category": "",
    "Name": "",
    "Date": "",
    "Start_Time": "",
    "End_Time": "",
    "Minutes": ""
}

active_task = []


def update_counter(counter_type: str, minutes: int):
    """
    Função que atualiza os valores padrões dos Contadores

        Args
        counter_type (str): informa a chave do dict
        counter_standard_minutes que será atualizada

        minutes (int): o novo valor em minutos que a chave terá

    """

    counter_standard_minutes[counter_type] = minutes


def end_counter(start_counter_time: datetime):
    """
    Função que registra no dicionário da atividade atual
    a hora de finalização do contador, e os minutos de diferença
    entre a hora inicial e final do contador.

    Args:
        start_counter_time (datetime): recebe a hora de início da task
        para calcular a diferença entre a hora de término da task.
    """

    end_counter_time = datetime.now()
    task["End_Time"] = end_counter_time.strftime("%H:%M")
    time_difference = end_counter_time - start_counter_time
    minutes = int(time_difference.total_seconds() / 60)
    task['Minutes'] = minutes


def start_counter():
    """
    Função que registra a hora e a data do inicio do contador
    Caso seja uma nova task

    Return
        start_counter_time (datetime): retorna a hora de início da task
    """
    start_counter_time = datetime.now()
    task["Date"] = start_counter_time.strftime("%d/%m/%Y")
    task["Start_Time"] = start_counter_time.strftime("%H:%M")

    return start_counter_time


def counter(counter_type: str, is_a_task: bool):
    """
    Função que inicia o contador

    Args:
        counter_type(str): informa a chave do dict counter_standard_minutes
        e pega o valor da contagem

        is_a_task(bool): verifica se o contador irá iniciar uma task ou
        período de descanso, caso seja task, deverá registrar data, hora
        inicial e hora final.
    """

    os.system('cls')
    if is_a_task:
        start_counter_time = start_counter()
        print("Select a Task")
        count = 0
        for t in active_task:
            print(f"[{count}] {t[0]}")
            count += 1
        print("-- ", end="")
        task_choosen = int(input())
        task["Name"] = active_task[task_choosen][0]
        task["Category"] = active_task[task_choosen][1]
        os.system('cls')
        print(f"Task: {task['Name']} | Category: {task['Category']}")
    else:
        print("Resting Time")

    seconds = counter_standard_minutes[counter_type] * 60

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")
        sleep(1)
        seconds -= 1
        if seconds == 0:
            if is_a_task:
                end_counter(start_counter_time)


def create_new_task():
    """
    Função que cria uma nova Task adicionando nome e categoria
    """
    os.system('cls')
    print("Create a new Task")
    task["Name"] = input("Name: ").title()
    category = input("[1] New Category [2] Existing Category \n-- ")
    if category == "1":
        task["Category"] = input("Category: ").title()
    else:
        # Caso seja uma Categoria existente, chama a função a seguir
        select_existing_category()

    cycles = input("N° of Cycles: ")

    existing_task = [task["Name"], task["Category"], f"{cycles}/{cycles}"]
    active_task.append(existing_task)

    app_menu()


def create_new_category():
    """
    Função que cria uma nova Category adicionando nome, dificuldade e cor
    """
    os.system('cls')
    print("Create a new Category")
    category = {
        "Name": "",
        "Difficulty": "",
        "Color": ""
    }
    for key in category.keys():
        category[key] = input(f"Category {key}: ")
    save_category(tuple(category.values()))


def select_existing_category():
    """
    Função que recebe as Categorias existentes do banco de dados
    exibe ao usuário e armazena a opção escolhida no dicionário.
    """
    all_categories = select_all_categories()
    count = 0
    for category in all_categories:
        print(f"[{count}] {category[0]}")
        count += 1
    category_choice = int(input("-- "))
    task["Category"] = all_categories[category_choice][0]


def app_menu():
    """
    Função que exibe o menu inicial e mostra as opções do app
    """
    os.system('cls')
    print("Hey Buddy!")
    print("[1] Pomodoro Counter | [2] Short Rest | [3] Long Rest")
    print("[4] New Category     | [5] New Task\n")
    print("~~ Active Tasks ~~")
    for task in active_task:
        print(f"{task[0]} | {task[1]} | {task[2]}")
    counter_type_choice = input("-- ")
    is_a_task = True
    if counter_type_choice == "1":
        counter("Pomodoro", is_a_task)
    elif counter_type_choice == "2":
        is_a_task = False
        counter("Short_Rest", is_a_task)
    elif counter_type_choice == "3":
        is_a_task = False
        counter("Long_Rest", is_a_task)
    elif counter_type_choice == "4":
        create_new_category()
    elif counter_type_choice == "5":
        create_new_task()
    else:
        print("Invalid Option")


app_menu()
# update_counter("short_rest", 1)
# counter("short_rest")
