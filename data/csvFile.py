import csv
import pandas as pd
from random import randint

filename = './resources/file_data.csv'


class WriteFile:
    def __init__(self) -> None:
        print("tested")

    @staticmethod
    def write_into_csv(emp_id=int, emp_name=str):
        with open(filename, 'a', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow([emp_id, emp_name])


class Reader:
    def __init__(self,   emp_id=int, emp_name=str) -> None:
        print("Reader")
        self.emp_id = emp_id
        self.emp_name = emp_name

    def read(self):
        df = pd.read_csv(filename)
        print(df)


reader = Reader(182, "niraj")
reader.read()
