import csv
import pandas as pd
from random import randint

filename = './resources/file_data.csv'
file_present = './resources/present.csv'


class WriteFile:
    @staticmethod
    def write_into_csv(emp_id) -> None:
        months = []
        for _ in range(12):
            months.append(randint(1, 12))

        data = ",".join(str(m) for m in months)

        with open(filename, 'a', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow([emp_id, data])

        with open(file_present, 'a', newline='\n') as file:
            present = randint(2, 90)
            absent = randint(0, 20)
            writer = csv.writer(file)
            writer.writerow([emp_id, present, absent])


class ReaderFile:
    def __init__(self,   emp_id: int) -> None:
        print("Reader")
        self.emp_id = emp_id

    def read(self):
        df = pd.read_csv(filename)
        print(df)
