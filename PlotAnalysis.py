import pandas as pd
import matplotlib.pyplot as plt
from SolarPowerModel import SolarPowerModel

csv_path="C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_2024_configured.csv"

class PlotAnalysis:
    def __init__(self, csv_path):
        self.solarpowermodel = SolarPowerModel(csv_path)
        self.data = self.solarpowermodel.load_data(usecols=['Month', 'Power'])

    def average_power_by_month(self):
        avg_power = self.data.groupby('Month')['Power'].mean()
        return avg_power
    
    def plot_power_vs_time(self):
        avg_power = self.average_power_by_month()

        if 'Power' not in self.data.columns or 'Month' not in self.data.columns:
            raise ValueError("Data must contain 'Power' and 'Month' columns for plotting.")

        plt.figure(figsize=(10, 6))
        plt.plot(avg_power.index, avg_power.values, label='Average Power by Month', color='orange', marker='o')
        plt.xlabel('Month of the Year')
        plt.xticks(avg_power.index)
        plt.ylabel('Power Output (W)')
        plt.ylim(0, max(avg_power.values) * 1.1)
        for x, y in zip(avg_power.index, avg_power.values):
            plt.annotate(f'{y:.1f}', (x, y), textcoords="offset points", xytext=(0,9), fontsize=8, ha='center', va='bottom')
        plt.title('Solar Panel Power Output vs Time')
        plt.legend()
        plt.grid(False)
        #plt.show()
        plt.savefig('solar_power_output.png')

if __name__ == "__main__":
    plotter = PlotAnalysis(csv_path)
    plotter.plot_power_vs_time()

    '''
    avg_power = plotter.average_power_by_month()
    print("Average Power by Month:")
    print(avg_power)
    '''