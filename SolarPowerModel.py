import pandas as pd

class SolarPowerModel:

    def __init__(self, csv_path = "nsrdb_configured.csv"):
        self.csv_path = csv_path
        self.data = None
    def __str__(self):
        if self.data is None:
            return "Solar Power Model: no data available"
        else:
            return f"Solar Power Model: {len(self.data)} rows"
        
    def load_data(self):
        self.data = pd.read_csv(self.csv_path)
        return self.data
    

if __name__ == "__main__":
    model = SolarPowerModel()
    df = model.load_data()
    print("Data Loaded")
    print(model)
    print(df.head())