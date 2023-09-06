import numpy as np
from sklearn.linear_model import LinearRegression
import time

# Simulated network traffic data
# In a real scenario, you would collect and preprocess actual network data.
timestamps = []
traffic_data = []

# Generate simulated data for demonstration purposes
for i in range(24):
    timestamps.append(i)
    # Simulate network traffic based on time of day (e.g., peak hours)
    if i >= 8 and i <= 18:
        traffic_data.append(np.random.randint(100, 500))
    else:
        traffic_data.append(np.random.randint(10, 50))

# Initialize a linear regression model
model = LinearRegression()

# Continuously monitor and optimize network traffic
while True:
    # Train the model with historical data
    X = np.array(timestamps).reshape(-1, 1)
    y = np.array(traffic_data)
    model.fit(X, y)

    # Predict network traffic for the next hour
    current_hour = int(time.strftime('%H'))
    next_hour = (current_hour + 1) % 24
    predicted_traffic = model.predict(np.array([[next_hour]]))

    # Perform network optimization based on predicted traffic
    # In a real scenario, this would involve adjusting network parameters, routing, or scaling resources.
    # For simplicity, we'll just print the prediction and sleep for an hour.
    print(f"Predicted Network Traffic for {next_hour}:00: {predicted_traffic[0]} Mbps")
    time.sleep(3600)  # Sleep for an hour
