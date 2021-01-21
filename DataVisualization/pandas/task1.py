import pandas as pd
import matplotlib.pyplot as plt
import json

# create the dataframes using the json file

df= pd.read_json('/DataVisualization/pandas/rain.json')
print(df)
print("\n\n\n\n")

df2 = pd.DataFrame(
    {
        "Cars":["Mitsubishi","Nissan","Hyundai"]
    }
)
print(df2)
print("\n\n\n")

print("df stats:\n" , df.describe())

df.plot(x='Month',y='Temperature')
plt.show()