import numpy as np 
from sklearn.neural_network import MLPClassifier 
from sklearn.preprocessing import StandardScaler 
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 
X = np.array([[18, 5], [20, 10], [22, 15], [25, 20],     [30, 35], [35, 40], [40, 50], [45, 60]]) 
y = np.array([0, 0, 0, 0, 1, 1, 1, 1]) 
scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X) 
model = MLPClassifier(     hidden_layer_sizes=(4,),     activation='relu',     solver='sgd',     learning_rate_init=0.01,     max_iter=5000,     random_state=42) 
model.fit(X_scaled, y) 
new_customer = np.array([[32, 38]]) 
new_customer_scaled = scaler.transform(new_customer) 
prediction = model.predict(new_customer_scaled) 
if prediction[0] == 1:     
    print("Prediction: Customer will PURCHASE") 
else:     
    print("Prediction: Customer will NOT PURCHASE") 
    df = pd.DataFrame(X, columns=["Age", "Spending Score"]) 
    df["Result"] = y 
    df["Result"] = df["Result"].map({0: "Not Purchased", 1: "Purchased"}) 
    sns.scatterplot(data=df, x="Age", y="Spending Score", hue="Result", style="Result", s=120) 
    sns.scatterplot(x=[32], y=[38], color="green", marker="X", s=250, label="New Customer") 
    plt.title("Neural Network Classification - Age vs Spending Score") 
    plt.show() 
