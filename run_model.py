from SolarPowerModel import SolarPowerModel

model = SolarPowerModel()

data = model.load_data()


print("Data loaded inside run_model.py!")
print(model)
print(data.head())