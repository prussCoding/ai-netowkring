import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Simulated network latency data
time_of_day = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # Time of day in hours
latency = np.array([50, 51, 52, 55, 58, 60, 65, 70, 75, 80])  # Latency in milliseconds

# Create a linear regression model
model = LinearRegression()

# Reshape the feature array (time_of_day) to match the input format
time_of_day = time_of_day.reshape(-1, 1)

# Train the model
model.fit(time_of_day, latency)

# Predict network latency for a specific time
predicted_time = 11  # Time of day in hours to predict latency
predicted_latency = model.predict([[predicted_time]])

# Plot the data and regression line
plt.scatter(time_of_day, latency, color='blue', label='Observed Latency')
plt.plot(time_of_day, model.predict(time_of_day), color='red', linestyle='--', label='Regression Line')
plt.scatter(predicted_time, predicted_latency, color='green', marker='o', label=f'Predicted Latency ({predicted_time}h)')
plt.xlabel('Time of Day (hours)')
plt.ylabel('Latency (ms)')
plt.legend()
plt.title('Network Latency Prediction with Linear Regression')
plt.show()

print(f'Predicted Latency at {predicted_time}h: {predicted_latency[0]:.2f} ms')
