import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate some sample data for demonstration purposes
# You would replace this with real network traffic data
# For simplicity, we'll use two features: time of day and day of week
# and predict network traffic volume.

# Sample data (time of day, day of week, network traffic)
data = np.array([
    [8, 1, 100],
    [12, 2, 200],
    [16, 3, 250],
    [20, 4, 180],
    [22, 5, 220],
    [10, 6, 150],
])

# Split the data into features (X) and target (y)
X = data[:, :-1]
y = data[:, -1]

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict network traffic for a specific time and day
new_data = np.array([[14, 3]])  # Predicting for 2 PM on a Wednesday
predicted_traffic = model.predict(new_data)

# Print the predicted traffic volume
print(f"Predicted Network Traffic: {predicted_traffic[0]} Mbps")

# Plot the data points and the regression line
plt.scatter(X[:, 0], y, color='blue', label='Actual Data')
plt.plot(X[:, 0], model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel('Time of Day')
plt.ylabel('Network Traffic (Mbps)')
plt.legend()
plt.title('Network Traffic Prediction with Linear Regression')
plt.show()

