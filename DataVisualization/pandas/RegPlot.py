import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./tempYearly.csv')
sns.set(rc={'figure.figsize':(12,6)})
sns.regplot(x='Year',y='Temperature',data=df)
plt.show()