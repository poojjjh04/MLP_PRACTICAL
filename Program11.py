from sklearn.cluster import KMeans 
import numpy as np 
data = np.array([[1, 40],[2, 45],[3, 50],[7, 75],[8, 80],[9, 85]]) 
model = KMeans(n_clusters=2, random_state=0, n_init=10) 
model.fit(data) 
clusters = model.predict(data) 
for i in range(len(data)):     
    print("Student", i + 1, "-> Cluster", clusters[i]) 
print("\nCluster Centers:") 
print(model.cluster_centers_) 
