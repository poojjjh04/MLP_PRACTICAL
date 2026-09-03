import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [35, 40, 50, 55, 65, 70, 80, 90]
model = LinearRegression()
model.fit(X,y)
hours = [[6.5]]
prediction = model.predict(hours)
print("Predicted Marks:", round(prediction[0], 2))
plt.scatter(X, y, label="Actual Data")
plt.plot(X, model.predict(X), label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Marks Obtained")
plt.title("Study Hours vs Marks")
plt.legend()
plt.show()
