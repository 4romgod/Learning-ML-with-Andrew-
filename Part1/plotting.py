import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


raw_training_data = pd.read_csv("train.csv")
raw_testing_data = pd.read_csv("test.csv")
train_data = raw_training_data.dropna()
test_data = raw_testing_data.dropna()

X = train_data['x']
Y = train_data['y']

X = np.array(X)
Y = np.array(Y)

# plotting the data
plt.title("Plot of Complete Data")
plt.xlabel("x values")
plt.ylabel("y values")
plt.plot(X, Y, "oc", label="data point")
plt.legend()
plt.show()