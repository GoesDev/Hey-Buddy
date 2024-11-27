import sqlite3


def connect_database():
    """
    Creates the connection to the Database

    Return
        conn (): database connection
    """
    conn = sqlite3.connect("app.db")
    return conn


def create_table_task():
    """
    Creates the Task table if it not exists
    """

    con = connect_database()
    cur = con.cursor()

    sql_create_task_table = """
        CREATE TABLE IF NOT EXISTS Task (
        Category TEXT NOT NULL,
        Name TEXT NOT NULL,
        Date TEXT NOT NULL,
        Start_Time TEXT NOT NULL,
        End_Time TEXT NOT NULL,
        Minutes INTEGER NOT NULL,
        FOREIGN KEY (Category) REFERENCES Category (Name)
        )
    """

    cur.execute(sql_create_task_table)
    con.commit()
    con.close()


def create_table_category():
    """
    Creates the Category table if it not exists
    """

    conn = connect_database()
    cur = conn.cursor()

    sql_create_category_table = """
        CREATE TABLE IF NOT EXISTS Category (
        Name TEXT PRIMARY KEY,
        Difficulty TEXT NOT NULL,
        Color TEXT NOT NULL
        )
    """

    cur.execute(sql_create_category_table)
    conn.commit()
    conn.close()


def save_task(new_task: tuple):
    """
    Adds a new task to the Database

    Args:
        new_task (tuple): task information
    """

    conn = connect_database()
    cur = conn.cursor()
    cur.execute('PRAGMA foreing_keys = ON')

    sql_insert_task = """
        INSERT INTO Task
        VALUES (?,
        ?,
        ?,
        ?,
        ?,
        ?)
    """

    cur.execute(sql_insert_task, new_task)
    conn.commit()
    conn.close()


def save_category(new_category: tuple):
    """
    Adds a new category to the Database

    Args:
        new_category (tuple): category information
    """

    conn = connect_database()
    cur = conn.cursor()

    sql_insert_category = """
        INSERT INTO category
        VALUES (?,
        ?,
        ?)
    """

    cur.execute(sql_insert_category, new_category)
    conn.commit()
    conn.close()


def update_category(att_category: tuple, category_name: str):
    """
    Receives a tuple with the category's new information and
    updates it in the database using the name as a reference.

    Args:
        att_category (tuple): category new stats
        category_name (str): name of the category to be changed
    """

    conn = connect_database()
    cur = conn.cursor()

    sql_update_category = """
        UPDATE Category
        SET Difficulty = ?,
            Color = ?
        WHERE name = ?
    """

    att_category += (category_name,)
    cur.execute(sql_update_category, att_category)
    conn.commit()
    conn.close()


def select_task(task_name: str):
    """
    Select a task from the Database and returns a tuple with its infos

    Args:
        task_name (string): name of an existing task in the database

    Return:
        task_info (tuple): task details
    """

    conn = connect_database()
    cur = conn.cursor()

    sql_select_task = """
        SELECT *
        FROM Task
        WHERE name = ?
    """

    cur.execute(sql_select_task, (task_name,))
    task_info = cur.fetchone()
    conn.close()
    return task_info


def select_category(category_name: str):
    """
    Select a category from the Database and returns a tuple with its infos

    Args:
        category_name (string): name of an existing task in the database

    Return:
        category_info (tuple): category details

    """

    conn = connect_database()
    cur = conn.cursor()

    sql_select_category = """
        SELECT *
        FROM Category
        WHERE Name = ?
    """

    cur.execute(sql_select_category, (category_name,))
    category_info = cur.fetchone()
    conn.close()
    return category_info


def select_all_tasks():
    """
    Função que seleciona todas as tasks do banco de dados
    e armazena em uma lista.

    Return:
        all_tasks (list): uma lista com todas as tasks em tuplas
    """
    conn = connect_database()
    cur = conn.cursor()

    sql_select_all_tasks = """
        SELECT *
        FROM Task
    """

    cur.execute(sql_select_all_tasks)
    all_tasks = cur.fetchall()
    return all_tasks


def select_all_categories():
    """
    Função que seleciona todas as categories do banco de dados
    e armazena em uma lista

    Return:
        all_categories (list): uma lista com todas as categories em tuplas
    """
    conn = connect_database()
    cur = conn.cursor()

    sql_select_all_categories = """
        SELECT *
        FROM Category
    """

    cur.execute(sql_select_all_categories)
    all_categories = cur.fetchall()
    return all_categories


def delete_task(task_name: str):
    """
    Select a task from the Database and delete its

    Args:
        task_name (string): name of an existing task in the database
    """

    conn = connect_database()
    cur = conn.cursor()

    sql_delete_task = """
        DELETE FROM Task
        WHERE Name = ?
    """

    cur.execute(sql_delete_task, (task_name,))
    conn.commit()
    conn.close()


def delete_category(category_name: str):
    """
    Select a category from the Database and delete its

    Args:
        category_name (string): name of an existing category in the database
    """

    conn = connect_database()
    cur = conn.cursor()

    sql_delete_category = """
        DELETE FROM Category
        WHERE Name = ?
    """
    cur.execute(sql_delete_category, (category_name,))
    conn.commit()
    conn.close()


# save_category(("Chess", "Easy", "Blue"))
# save_task(('Chess', 'Playing Chess', '21/11/2024', '16:45', '17:10', '25',))
# create_table_category()
# create_table_task()
# update_category(("Easy", "Blue"), "Chess")
# task = select_category("Chess")
# print(task)
# delete_category("Chess")
# delete_task("2x Chess Games")
# delete_task("name")
# delete_category("Python")
# delete_category("English")

# category = select_category("Python")
# print(category)

# categories = select_all_categories()
# print(type(categories))
# for category in categories:
#     print(category)

# print(categories[0][0])
