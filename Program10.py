from sklearn.neighbors import KNeighborsClassifier 
X = [[2, 60, 45], [3, 65, 50],[4, 70, 55],[5, 75, 60],[6, 80, 65],[7, 85, 70],[8, 90, 80],[9, 95, 85]] 
y = ["Fail","Fail","Fail","Pass","Pass","Pass","Pass","Pass"] 
knn = KNeighborsClassifier(n_neighbors=3) 
knn.fit(X, y) 
new_student = [[6, 82, 68]] 
prediction = knn.predict(new_student) 
print("New Student Details:") 
print("Study Hours:", new_student[0][0]) 
print("Attendance:", new_student[0][1], "%") 
print("Previous Test Mark:", new_student[0][2]) 
print("Predicted Result:", prediction[0])
