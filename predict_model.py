from SolarPowerModel import SolarPowerModel
from train_model import train_model

model = SolarPowerModel()
data = model.load_data()


w = train_model(data)

ghi_val = float(input("Enter a GHI value: "))
predicted_power = ghi_val * w.item()
print(f"{ghi_val} = {predicted_power}" )