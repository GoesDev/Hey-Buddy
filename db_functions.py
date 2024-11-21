import sqlite3


def connect_database():
    """
    Creates the connection to the Database
    """
    conn = sqlite3.connect("app.db")
    return conn


def create_table_activity():
    """
    Creates the Activity table if it not exists
    """

    con = connect_database()
    cur = con.cursor()

    sql_create_activity_table = """
        CREATE TABLE IF NOT EXISTS Activity (
        Name TEXT NOT NULL,
        Date TEXT NOT NULL,
        Start_Time TEXT NOT NULL,
        End_Time TEXT NOT NULL,
        Minutes INTEGER NOT NULL,
        Category TEXT UNIQUE,
        FOREIGN KEY (Category) REFERENCES Category (Name)
        )
    """

    cur.execute(sql_create_activity_table)
    con.commit()
    con.close()


def create_table_category():
    """
    Creates the Category table if it not exists
    """

    con = connect_database()
    cur = con.cursor()

    sql_create_category_table = """
        CREATE TABLE IF NOT EXISTS Category (
        Name TEXT UNIQUE PRIMARY KEY,
        Difficulty TEXT NOT NULL,
        Color TEXT NOT NULL
        )
    """

    cur.execute(sql_create_category_table)
    con.commit()
    con.close()


def save_activity(new_activity):
    """
    Adds a new activity to the Database

    Args:
        new_activity (tuple): activity information
    """

    con = connect_database()
    cur = con.cursor()
    cur.execute('PRAGMA foreing_keys = ON')

    sql_insert_activity = """
        INSERT INTO activity
        VALUES (?,
        ?,
        ?,
        ?,
        ?,
        ?)
    """

    cur.execute(sql_insert_activity, new_activity)
    con.commit()
    con.close()


def save_category(new_category):
    """
    Adds a new category to the Database

    Args:
        new_category (tuple): category information
    """

    con = connect_database()
    cur = con.cursor()

    sql_insert_category = """
        INSERT INTO category
        VALUES (?,
        ?,
        ?)
    """

    cur.execute(sql_insert_category, new_category)
    con.commit()
    con.close()


def update_character(att_character):
    """
    Receives a tuple with the character's new information and
    updates it in the database using the name as a reference.

    Args:
        att_character (tuple): character new stats
    """

    con = connect_database()
    cur = con.cursor()

    sql_update_character = """
        UPDATE character
        SET level = ?,
            life = ?,
            attack = ?,
            defense = ?,
            gold = ?,
            special_abilities = ?,
            clues = ?,
            equipament = ?
        WHERE name = ?
    """

    cur.execute(sql_update_character, att_character)
    con.commit()
    con.close()


def select_character(character_name):
    """
    Select a character from the Database and returns a tuple with its stats

    Args:
        character_name (string): name of an existing character in the database

    Return:
        character_sheet (tuple): character stats
    """

    conn = connect_database()
    cur = conn.cursor()

    sql_select_character = """
        SELECT *
        FROM character
        WHERE name = ?
    """

    cur.execute(sql_select_character, (character_name,))
    character_sheet = cur.fetchone()
    conn.close()
    return character_sheet


def delete_character(character_name):
    """
    Select a character from the Database and delete its

    Args:
        character_name (string): name of an existing character in the database
    """

    con = connect_database()
    cur = con.cursor()

    sql_delete_character = """
        DELETE FROM character
        WHERE name = ?
    """

    cur.execute(sql_delete_character, (character_name,))
    con.commit()
    con.close()


# save_category(("chess", "easy", "blue"))
# save_activity(('2x game','21/11/2024','16:45', '17:10', '25', 'chess'))
# create_table_category()
# create_table_activity()
