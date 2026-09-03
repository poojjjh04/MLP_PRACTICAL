from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score, confusion_matrix 
from sklearn.metrics import classification_report 
import matplotlib.pyplot as plt 
X = [[22], [25], [28], [30], [35],[40], [45], [50], [55], [60]] 
y = [0, 0, 0, 0, 0,1, 1, 1, 1, 1] 
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=42) 
model = LogisticRegression() 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
print("Accuracy:", accuracy_score(y_test, y_pred)) 
print("Confusion Matrix:") 
print(confusion_matrix(y_test, y_pred)) 
print("Classification Report:") 
print(classification_report(y_test, y_pred)) 
plt.scatter(X, y, label="Actual Data") 
plt.scatter(X_test, y_pred, marker="x", label="Predicted Data") 
plt.xlabel("Age") 
plt.ylabel("Class") 
plt.title("Logistic Regression Classification") 
plt.legend() 
plt.show()
