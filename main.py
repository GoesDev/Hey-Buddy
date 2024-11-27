from time import sleep
from db_functions import save_category, select_all_categories
from task import Task
import os
os.system('cls')

# DICIONÁRIO COM OS VALORES PADRÕES DOS CONTADORES
# PODE SER ALTERADO PELA FUNÇÃO update_counter()
counter_standard_minutes = {
    "Pomodoro": 1,
    "Short_Rest": 5,
    "Long_Rest": 15
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


def end_counter(task_chosen: int):
    """
    Função que registra no dicionário da atividade atual
    a hora de finalização do contador, e os minutos de diferença
    entre a hora inicial e final do contador.

    Args:
    """

    task = active_task[task_chosen]
    task.end_time()


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
        print("Select a Task")
        count = 0
        for task in active_task:
            print(f"[{task.name.title()}")
            count += 1
        print("-- ", end="")
        task_chosen = int(input())
        task = active_task[task_chosen]
        task.start_time()
        os.system('cls')
        print(f"Task: {task.name} | Category: {task.category}")
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
                end_counter(task_chosen)


def create_new_task():
    """
    Função que cria uma nova Task adicionando nome e categoria
    """
    os.system('cls')
    print("Create a new Task")
    task_name = input("Name: ").title()
    category = input("[1] New Category [2] Existing Category \n-- ")
    if category == "1":
        task_category = input("Category: ").title()
    else:
        # Caso seja uma Categoria existente, chama a função a seguir
        task_category = select_existing_category()

    cycles = input("N° of Cycles: ")

    new_task = Task(task_name, task_category, cycles)

    active_task.append(new_task)


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
    task_category = all_categories[category_choice][0]
    return task_category


def app_menu():
    """
    Função que exibe o menu inicial e mostra as opções do app
    """
    app_on = True
    while app_on is True:
        os.system('cls')
        print("Hey Buddy!")
        print("[1] Pomodoro Counter | [2] Short Rest | [3] Long Rest")
        print("[4] New Category     | [5] New Task\n")
        print("Press 'q' to quit")
        print("\n~~ Active Tasks ~~")
        # print(active_task)
        for task in active_task:
            print(f"{task.name}",
                  f" | {task.category}",
                  f" | {task.current_cycle}/{task.total_cycles}")
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
        elif counter_type_choice == 'q':
            app_on = False
            break
        else:
            print("Invalid Option")


app_menu()
# update_counter("short_rest", 1)
# counter("short_rest")
