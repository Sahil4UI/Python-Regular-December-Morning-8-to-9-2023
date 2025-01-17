import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('appl_1980_2014.csv')
print(dataset.head())

X = pd.to_datetime(dataset['Date'])
Y = dataset['Adj Close']
# line plot
plt.plot(X,Y)
plt.show()