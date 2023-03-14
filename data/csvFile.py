import csv


def write_into_csv(emp_id=int, emp_name=str):
    with open('./resources/file_data.csv', 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([emp_id, emp_name])
