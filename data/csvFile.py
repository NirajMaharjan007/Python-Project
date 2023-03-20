import csv


class WriteFile:
    def __init__(self):
        print("tested")

    def write_into_csv(self,emp_id=int, emp_name=str):
        with open('./resources/file_data.csv', 'a', newline='\n') as file:
            writer = csv.w
            writer.writerow([emp_id, emp_name])
            
