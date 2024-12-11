import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load Dataset
iris = load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Labels (0: Setosa, 1: Versicolor, 2: Virginica)

# Step 2: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Choose Number of Neighbors (k)
k = 3

# Step 4: Initialize and Train kNN Model
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Step 5: Make Predictions
y_pred = knn.predict(X_test)

# Step 6: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))

# Step 7: Predict for New Data
new_samples = np.array([[5.1, 3.5, 1.4, 0.2],  # Likely Setosa
                         [6.5, 3.0, 5.2, 2.0]])  # Likely Virginica
predictions = knn.predict(new_samples)
predicted_species = [iris.target_names[p] for p in predictions]
print("\nNew Sample Predictions:", predicted_species)

# Optional: Visualize Feature Importance (if relevant for an extended project)
# This step is usually not applicable to kNN, but you can visualize relationships using scatter plots, etc.
if __name__ == "__main__":
    print("kNN Project Completed.")
