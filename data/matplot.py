import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Graph:
    def __init__(self, emp_id: int, name: str):
        file_name = "./resources/file_data.csv"
        csv = pd.read_csv(file_name)
        self.emp_id = emp_id
        self.name = name

        self.df = pd.DataFrame(csv)

    def plot(self):
        try:
            row_num = self.df.loc[self.df['emp_id'] == self.emp_id].index[0]
            row_to_plot = self.df.iloc[row_num, 1:]

            fig, ax = plt.subplots()

            ax.bar(row_to_plot.index, row_to_plot.values)

            ax.set_title("Data for: " + self.name)
            ax.set_xlabel("Month")
            ax.set_ylabel("Perfomance")

            plt.show()

        except Exception as e:
            print(e)
            return None


class PieChart:
    def __init__(self, emp_id: int, name: str):
        self.emp_id = emp_id
        self.name = name

        file_name = "./resources/present.csv"
        csv = pd.read_csv(file_name)

        self.df = pd.DataFrame(csv)

    def plot(self):
        try:
            row_num = self.df.loc[self.df['emp_id'] == self.emp_id].index[0]
            row_to_plot = self.df.iloc[row_num, 1:]

            y = np.array(row_to_plot)

            mylabels = ["Present", "Absent"]

            print(y)

            fig, pie_chart = plt.subplots()

            pie_chart.set_title("Attendance for: " + self.name)
            pie_chart.pie(y, labels=mylabels, startangle=90, autopct='%1.1f%%')

            plt.show()

        except Exception as e:
            print(e)
            return None
