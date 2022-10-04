import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('casas.csv')

X = df.drop('preco', axis=1)
y = df['preco']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = LinearRegression()
modelo = modelo.fit(X_train, y_train)

input = open("modelo-salvo", "wb")
pickle.dump(modelo, input)
input.close()
