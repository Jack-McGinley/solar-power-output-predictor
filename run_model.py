import time
from SolarPowerModel import SolarPowerModel
from train_model import train_model
from pprint import pprint
import pandas as pd
import os

#csv_path ="C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_2024_configured.csv"

def compare_monthly(true_list, pred_list):
    return list(map(lambda t, p: abs(t-p), true_list, pred_list))

class RunModel:
    def __init__(self, csv_path):
        #Load data and train model
        self.csv_path = csv_path
        self.model = SolarPowerModel(csv_path)
        self.data = self.model.load_data()
        self.w = train_model(self.data) #The learned weight tensor is returned
        self.monthly_summary = None

    def compute_stats(self):
        # Convert tensor (or similar) to a scalar
        try:
            w_value = self.w.item()
        except AttributeError:
            # Fallback if it's already a float / numpy scalar
            w_value = float(self.w)

        #New column for Prediced Power
        self.data["PredictedPower"] = self.data["GHI"]*w_value

        #Compute monthly averages
        true_montly_avg = self.data.groupby("Month")["Power"].mean().tolist()
        pred_monthly_avg = self.data.groupby("Month")["PredictedPower"].mean().tolist()


        print(f"True Monthly Average Power: ", [f'{val:.4f}' for val in true_montly_avg])
        time.sleep(1)  # Pause for 1 second for better user experience
        print(f"Predicted Monthly Average Power: ", [f'{val:.4f}' for val in pred_monthly_avg])
        #Compare true vs predicted monthly averages 
        difference = compare_monthly(true_montly_avg,pred_monthly_avg)
        time.sleep(1)  # Pause for 1 second for better user experience
        print("The differnce of values are presented in the list below")
        format_list = [f'{val:.4f}' for val in difference]
        pprint(format_list)

        # Build summary DataFrame
        months = sorted(self.data["Month"].unique())
        self.monthly_summary = pd.DataFrame({
            "Month": months,
            "TrueMonthlyAvg": true_montly_avg,
            "PredMonthlyAvg": pred_monthly_avg,
            "Difference": difference
        })

        return self.monthly_summary

    def save_monthly_summary(self, output_path=None):
        #Save the monthly comparison DataFrame to a CSV file.
        if self.monthly_summary is None:
            raise ValueError("Error: compute_stats() must be run before saving monthly summary.")
            # Same folder as the input CSV, new file name
        if output_path is None:
            folder = os.path.dirname(os.path.abspath(self.csv_path))
            output_path = os.path.join(folder, "monthly_summary.csv")
            self.monthly_summary.to_csv(output_path, index=False)
            print(f"Monthly summary saved to: {output_path}")

if __name__ == "__main__":
    # Put your CSV path here or pass via sys.argv in the future
    csv_path = "C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_2024_configured.csv"

    runner = RunModel(csv_path)
    runner.compute_stats()
    runner.save_monthly_summary()



    