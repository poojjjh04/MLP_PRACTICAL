from sklearn.tree import DecisionTreeClassifier 
study_hours = [[1], [2], [3], [4], [5], [6]] 
result = [0, 0, 1, 1, 1, 1] 
model = DecisionTreeClassifier() 
model.fit(study_hours, result) 
new_student = [[3.5]] 
prediction = model.predict(new_student) 
if prediction[0] == 1:     
    print("Student will PASS") 
else:    
    print("Student will FAIL") 
