import csv

filename = './resources/file_data.csv'


class WriteFile:
    def __init__(self):
        print("tested")

    def write_into_csv(self, emp_id=int, emp_name=str):
        with open(filename, 'a', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow([emp_id, emp_name])


class Reader:
    def __init__(self) -> None:
        print("Reader")

    def read_csv(self,  emp_id=int, emp_name=str):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
