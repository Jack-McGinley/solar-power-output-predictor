import pandas as pd
import os
#print(os.getcwd())

class Data_Config:
    def __init__(self, nsrdb_file, area=1.6, efficiency=0.2, temp_coeff=-0.0045, noct=45):
        #attribute for nsrdb file path
        self.nsrdb_file = nsrdb_file
        self.sample = None
        self.area = area
        self.efficiency = efficiency
        self.temp_coeff = temp_coeff
        self.noct = noct

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
        cleaned_sample = df_cleaned_columns.dropna(how='any', subset=['GHI', 'Temperature'], axis=0)
        #return cleaned sample
        self.sample = cleaned_sample
        return self.sample

    def ML_Info(self):
        #Remove Year and Minute columns
        df = self.sample.drop(columns=['Year', 'Minute'], errors='ignore')
        #Remove rows where Hour is between 0 and 8 (inclusive)
        if 'Hour' in df.columns:
            df = df[df['Hour'] > 8]
        #Reset index and save cleaned df
        df = df.reset_index(drop=True)
        self.sample = df
        return self.sample

    def power(self):
        #Calculate power using Solar Panel Module parameters and dataset
        df = self.sample.copy() #Use a copy to avoid modifying original sample, parenthesis added to ensure df is a dataframe and not a function
        #Set parameters
        area = self.area
        efficiency = self.efficiency
        temp_coeff = self.temp_coeff
        noct = self.noct
        #Collect necessary columns
        G = df['GHI']
        T = df['Temperature']
        #Use formula to calculate power
        T_cell = T + (noct - 20) / 800 * G
        P = area * efficiency * G * (1 + temp_coeff * (T_cell - 25))
        #Add power column to dataframe
        df['Power'] = P
        #return dataframe with power column
        self.sample = df
        return self.sample
    
    def configure_sample(self):
        self.load_sample()
        self.clean_dataset()
        self.ML_Info()
        data = self.power()
        return data
    
    def configure(self):
        self.load_file()
        self.clean_dataset()
        self.ML_Info()
        data = self.power()
        return data

#Test the Data_Config class
'''
if __name__ == "__main__":
    dc = Data_Config("C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_2024.csv")
    #sample = dc.load_sample()
    #sample_cleaned = dc.clean_dataset()
    #sample_ml = dc.ML_Info()
    sample_output = dc.configure_sample()
    #print(sample.to_string())
    #print(sample_ml.to_string())
    print(sample_output.to_string())

    print("Raw shape:", sample.shape)
    print("Cleaned shape:", sample_cleaned.shape)
    print("ML shape:", sample_ml.shape)
'''


#Configure data using configure method
dc = Data_Config("C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_2024.csv")
data_ml = dc.configure()
data_ml.to_csv("C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_configured.csv", index=False)

