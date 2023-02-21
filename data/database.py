from mysql.connector import connect


def get_connection():
    try:
        conn = connect(
            host="localhost",
            user="root",
            password="",
            database="my_database"
        )
        return conn

    except Exception as err:
        print(err)
        return None


def get_login(username, password):
    global u, p
    u = username
    p = password
    conn = get_connection()

    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        if result is not None:
            return True
        else:
            return False
    else:
        return False


def get_adminId():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM users WHERE username = %s AND password = %s", (u, p))
        result = cursor.fetchone()

        if result is not None:
            return result[0]

    except Exception as err:
        print(err)


class Employee:
    def __init__(self):
        try:
            if get_connection() is not None:
                pass
            else:
                raise Exception("Can not set to database")
        except Exception as err:
            print(err)
