import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


file_name = "./resources/file_data.csv"
csv = pd.read_csv(file_name)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class BarGraph:
    def __init__(self, emp_id: int, name: str):
        self.emp_id = emp_id
        self.name = name

        self.df = pd.DataFrame(csv)

    def plot(self):
        try:
            row_num = self.df.loc[self.df['emp_id'] == self.emp_id].index[0]
            row_to_plot = self.df.iloc[row_num, 2:]
            fig, ax = plt.subplots()
            ax.bar(row_to_plot.index, row_to_plot.values)

            ax.set_title("Data for id: " + self.name)
            ax.set_xlabel("Month")
            ax.set_ylabel("Value")

            plt.show()

        except Exception as e:
            print(e)
            return None
