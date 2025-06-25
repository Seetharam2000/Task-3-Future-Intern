import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Iris.csv')
data = df['SepalLengthCm']
plt.hist(data, bins=20, color='DarkBlue', edgecolor='White')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length in Iris Dataset')
plt.show()