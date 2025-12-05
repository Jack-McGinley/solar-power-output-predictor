from SolarPowerModel import SolarPowerModel
from train_model import train_model


def compare_monthly(true_list, pred_list):
    return list(map(lambda t, p: abs(t-p), true_list, pred_list))

#Load data and train model
model = SolarPowerModel()

data = model.load_data()
w = train_model(data) #The learned weight tensor is returned

print("Data loaded inside run_model.py!")
print(model)
print(data.head())

w_value = w.item() # convert tensor weight into normal value
#New column for Prediced Power
data["PredictedPower"] = data["GHI"]*w_value

#Compute monthly averages

true_montly_avg = data.groupby("Month")["Power"].mean().tolist()

pred_monthly_avg = data.groupby("Month")["PredictedPower"].mean().tolist()


print(f"True Monthly Average Power: {true_montly_avg}")
print(f"Predicted Monthly Average Power: {pred_monthly_avg}")

#Compare true vs predicted monthly averages 
difference = compare_monthly(true_montly_avg,pred_monthly_avg)

print("The differnce of values are presented in the list below")
print(difference)




    