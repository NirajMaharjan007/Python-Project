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
            "SELECT * FROM admins WHERE name = %s AND password = %s", (username, password))
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
            "SELECT id FROM admins WHERE name = %s AND password = %s", (u, p))
        result = cursor.fetchone()

        if result is not None:
            return result[0]

    except Exception as err:
        print(err)


class Employee:
    def __init__(self):
        try:
            self.conn = get_connection()
            if self.conn is not None:
                self.cur = self.conn.cursor()
            else:
                raise Exception("Can not set to database")
        except Exception as err:
            print(err)

    def get_count(self):
        try:
            self.cur.execute("SELECT COUNT(*) FROM employees")
            result = self.cur.fetchone()[0]
            if result is not None:
                return result
            else:
                raise ("Did not find employee; Error")

        except Exception as err:
            print(err)
            return -1
