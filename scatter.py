import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("SaratogaHouses.csv")
print(dataset.head())

x = dataset['livingArea']
y = dataset['price']
plt.title("Price WRT LIVING AREA")
plt.xlabel("Living Area")
plt.ylabel("Price")
plt.scatter(x,y)
plt.show()

