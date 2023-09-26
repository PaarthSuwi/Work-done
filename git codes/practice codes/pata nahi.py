import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
data = pd.read_csv("data.csv")

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data.drop("target", axis=1), data["target"], test_size=0.2)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))

# Plot the confusion matrix
plt.figure()
plot_confusion_matrix(y_test, y_pred)
plt.show()