import pandas as pd
import matplotlib.pyplot as plt
from SolarPowerModel import SolarPowerModel

class PlotAnalysis:
    """
    PlotAnalysis class to handle plotting and analysis of solar panel power output data.
    It uses the SolarPowerModel class to load the configured data and uses the mean aggregate 
    function to calculate average power by month and plot power output over time for the
    configured dataset.
    """
    def __init__(self, csv_path):
        self.solarpowermodel = SolarPowerModel(csv_path)
        self.data = self.solarpowermodel.load_data(usecols=['Month', 'Power'])

    def average_power_by_month(self):
        """
        Calculate the average power output by month.
        Returns:
            pd.Series: The average power output for each month.
        """
        avg_power = self.data.groupby('Month')['Power'].mean() #Calculate average power by month
        return avg_power
    
    def plot_power_vs_time(self):
        """
        Plot the average power output by month over time.
        Saves the plot as 'solar_power_output.png'.
        """
        avg_power = self.average_power_by_month() #Get average power by month

        if 'Power' not in self.data.columns or 'Month' not in self.data.columns: #ensure appropriate columns exist
            raise ValueError("Data must contain 'Power' and 'Month' columns for plotting.")

        #plot the average power by month
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
