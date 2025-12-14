"""
This file defines the SolarPowerModel class.
The class is responsible for loading the solar dataset froma CSV file
and storing it as pandas DataFrame for further processing.

This class only handles data loading and basic info about dataset.
"""


import pandas as pd

csv_path ="C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_2024.csv"

class SolarPowerModel:
    """A simple class for loading and managing solar power data"""

    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.data = None
    def __str__(self):
        """Returns a string representation of the model"""
        if self.data is None:
            return "Solar Power Model: no data available"
        else:
            return f"Solar Power Model: {len(self.data)} rows"
    #Read the CSV file using pandas   
    def load_data(self, **kwargs):
        self.data = pd.read_csv(self.csv_path, **kwargs)
        return self.data
    
#Runs only when this file is executed directly
if __name__ == "__main__":
    model = SolarPowerModel(csv_path)
    df = model.load_data()
    print("Data Loaded")
    print(model)
    print(df.head())