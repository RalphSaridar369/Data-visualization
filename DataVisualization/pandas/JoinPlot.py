import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./tempYearly.csv')
print(df)

sns.jointplot("Rainfall","Temperature",data=df, kind="hex")
sns.jointplot("Rainfall","Temperature",data=df, kind="reg")
plt.show()