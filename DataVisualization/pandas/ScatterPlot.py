import pandas as pd
import matplotlib.pyplot as plt
import seaborn

df = pd.read_json('./rain.json')

plt.figure(figsize=(25,5))
plt.plot(df['Month'] ,df['Temperature'] ,label='Temperature')
plt.show()

plt.figure(figsize=(25,5))
plt.plot(df['Month'] ,df['Rainfall'] ,label='Rainfall')
plt.show()


#plot together

plt.figure(figsize=(25,5))
plt.plot(df['Month'] ,df['Rainfall'] ,label='Rainfall')
plt.plot(df['Month'] ,df['Temperature'] ,label='Temperature')
plt.legend()
plt.show()