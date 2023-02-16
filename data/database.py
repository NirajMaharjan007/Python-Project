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
