from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
import pandas as pd

# fetch dataset
heart_disease = fetch_ucirepo(id=45)
hd = pd.read_csv('heart_disease')
df = pd.DataFrame(hd)
print(df)

"""
# data (as pandas dataframes)
X = heart_disease.data.features
y = heart_disease.data.targets

plt.figure(figsize=(10,5))
plt.plot()
# metadata
print(heart_disease.metadata)

# variable information
print(heart_disease.variables)

print()
print("Heart Disease Demo using Matplot Line Graph")
print()

"""