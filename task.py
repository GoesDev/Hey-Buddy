from datetime import datetime
from db_functions import save_task


class Task():

    def __init__(self, name, category, cycles) -> None:
        """
        Inicializa os atributos de uma Task
        """
        self.name = name
        self.category = category
        self.total_cycles = cycles
        self.current_cycle = 0

    def start_time(self):
        """
        Função que registra a data e hora inicial ao iniciar a Task
        """
        self.start_counter_time = datetime.now()
        self.date = self.start_counter_time.strftime("%d/%m/%Y")
        self.start_t = self.start_counter_time.strftime("%H:%M")

    def end_time(self):
        """
        Função que registra a hora final e os minutos de diferença ao
        finalizar uma Task
        """
        self.end_counter_time = datetime.now()
        self.end_t = self.end_counter_time.strftime("%H:%M")
        time_difference = self.end_counter_time - self.start_counter_time
        self.minutes = int(time_difference.total_seconds() / 60)

    def save_task(self):

        task_data = (
            self.category,
            self.name,
            self.date,
            self.start_t,
            self.end_t,
            self.minutes
        )

        save_task(task_data)
