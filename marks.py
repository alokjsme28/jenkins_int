import pandas as pd
from sklearn.linear_model import LinearRegression
ds = pd.read_csv("marks.csv")
model = LinearRegression()
x = ds["Hrs"]
Y = ds["Marks"]
X = x.values.reshape(4,1)
model.fit(X,Y)
mind.coef_
mind.predict([[9]]) 