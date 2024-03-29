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
    count: int

    def __init__(self):
        try:
            self.conn = get_connection()
            if self.conn is not None:
                self.cur = self.conn.cursor()
            else:
                raise Exception("Can not set to database")
        except Exception as err:
            print(err)

        self.count = self.get_count()

    def get_count(self):
        try:
            admin_id = get_adminId()
            self.cur.execute(
                f"SELECT COUNT(*) FROM employees WHERE admin_id = '{admin_id}'")
            result = self.cur.fetchone()[0]
            if result is not None:
                return result
            else:
                raise ("Did not find employee; Error")

        except Exception as err:
            print(err)
            return -1

    def set_employee(self, emp_id, name, address, email, dob, gender, phone):
        try:
            admin_id = get_adminId()
            sql = f"INSERT INTO employees VALUES ('{emp_id}', '{name}', '{address}', '{email}', '{dob}', '{gender}', '{phone}', '{admin_id}')"
            print(sql)
            self.cur.execute(sql)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)
            return False

    def get_employee_detail(self):
        try:
            admin_id = get_adminId()
            query = f"SELECT emp_id,emp_name,address,email,dob,gender,phone_no FROM employees where admin_id = {admin_id}"
            self.cur.execute(query)
            result = self.cur.fetchall()
            return result

        except Exception as err:
            print("Error =>", err)
            return None

    def update_info(self, emp_id, name, address, email, dob, gender, phone):
        try:
            print(emp_id)
            sql = f"Update employees set emp_name = '{name}',address='{address}',email='{email}',dob='{dob}',gender='{gender}',phone_no='{phone}' where emp_id = '{emp_id}'"
            self.cur.execute(sql)
            self.conn.commit()
            return True

        except Exception as err:
            print("Error =>", err)
            return False

    def delete(self, emp_id=int):
        try:
            query = f"DELETE FROM employees WHERE emp_id='{emp_id}'"
            self.cur.execute(query)
            num_deleted_rows = self.cur.rowcount
            self.conn.commit()

            if num_deleted_rows > 0:
                print("Rows were deleted")
                return True

            else:
                raise Exception("Can not delete employee")

        except Exception as err:
            print("Error =>", err)
            return False

    def get_performance(self):
        try:
            admin_id = get_adminId()
            sql = "SELECT employees.emp_id, emp_name,performance.result,\
                performance.attitude, performance.project_completed \
                FROM employees LEFT JOIN \
                performance ON employees.emp_id = performance.emp_id\
                where admin_id = " + str(admin_id)

            self.cur.execute(sql)
            result = self.cur.fetchall()
            return result

        except Exception as err:
            print("Error =>", err)
            return None

    def insert_performance(self, emp_id=int, result=int, attitude=int, project_completed=int):
        try:
            sql = f"INSERT INTO performance(emp_id,result,attitude,project_completed)\
                values ({emp_id},{result} ,{attitude}, {project_completed})"

            self.cur.execute(sql)
            self.conn.commit()
            return True
        except Exception as err:
            print("Error =>", err)
            return False

    def update_performance(self, emp_id=int, result=int, attitude=int, project_completed=int):
        try:
            sql = f"update performance set result = {result},\
                project_completed = {project_completed}, attitude = {attitude}\
                    where emp_id={emp_id}"
            self.cur.execute(sql)
            self.conn.commit()
            return True
        except Exception as err:
            print("Error =>", err)
            return False

    def get_emp_name(self, id=int) -> str:
        try:
            sql = f"select emp_name from employees where emp_id={id}"
            self.cur.execute(sql)
            result = self.cur.fetchone()[0]

            if result is not None:
                return result

            else:
                raise Exception("Emp_name not found in employees table")

        except Exception as err:
            print("Error =>", err)
            return None
