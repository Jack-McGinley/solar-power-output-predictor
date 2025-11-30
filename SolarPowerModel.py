import pandas as pd

csv_path ="C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_2024.csv"

class SolarPowerModel:

    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.data = None
    def __str__(self):
        if self.data is None:
            return "Solar Power Model: no data available"
        else:
            return f"Solar Power Model: {len(self.data)} rows"
        
    def load_data(self, **kwargs):
        self.data = pd.read_csv(self.csv_path, **kwargs)
        return self.data
    

if __name__ == "__main__":
    model = SolarPowerModel(csv_path)
    df = model.load_data()
    print("Data Loaded")
    print(model)
    print(df.head())