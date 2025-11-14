import pandas as pd
import os
#print(os.getcwd())

class Data_Config:
    def __init__(self, nsrdb_file):
        #attribute for nsrdb file path
        self.nsrdb_file = nsrdb_file
        self.sample = None

    def load_sample(self):
        #load first 50 rows after skipping first 2 metadata rows
        self.sample = pd.read_csv(self.nsrdb_file, header=2,nrows=50)
        #return sample dataframe for testing
        return self.sample
    
    def load_file(self):
        #load file after skipping first 2 metadata rows
        self.sample = pd.read_csv(self.nsrdb_file, header=2)
        #return sample dataframe for testing
        return self.sample

    def clean_dataset(self):
        #remove columns with all NaN values
        df_cleaned_columns = self.sample.dropna(how='all', axis=1)
        #remove rows with any NaN values
        cleaned_sample = df_cleaned_columns.dropna(how='any', axis=0)
        #return cleaned sample
        self.sample = cleaned_sample
        return self.sample

    def ML_Info(self):
        #Remove Year and Minute columns
        df = self.sample.drop(columns=['Year', 'Minute'], errors='ignore')
        #Remove rows where Hour is between 0 and 8 (inclusive)
        df = df[df['Hour'] > 8]
        #Reset index and save cleaned df
        df = df.reset_index(drop=True)
        self.sample = df
        return self.sample

    def configure(self):
        self.load_file()
        self.clean_dataset()
        data = self.ML_Info()
        return data

#Test the Data_Config class
"""
if __name__ == "__main__":
    dc = Data_Config("C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_2024.csv")
    sample = dc.load_sample()
    sample_cleaned = dc.clean_dataset()
    sample_ml = dc.ML_Info()
    print(sample_ml.to_string())

    print("Raw shape:", sample.shape)
    print("Cleaned shape:", sample_cleaned.shape)
    print("ML shape:", sample_ml.shape)
"""

#Configure data using configure method
dc = Data_Config("C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_2024.csv")
data_ml = dc.configure()
data_ml.to_csv("C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_configured.csv", index=False)

