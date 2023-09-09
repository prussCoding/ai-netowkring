import numpy as np
from sklearn.linear_model import LinearRegression
import time
import logging

# Set logging basic configuration
logging.basicConfig(format='%(levelname)s:  %(message)s', level=logging.DEBUG)


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

 # Train the model with historical data
X = np.array(timestamps).reshape(-1, 1)
y = np.array(traffic_data)

model.fit(X, y)

# Setting Current hour
current_hour = 1
# Setting Predicted_hours
predicted_hours = 23
# Setting Bandwidth
bandwidth = 500

# Continuously monitor and optimize network traffic
while True and current_hour <= predicted_hours:
   
    # Predict network traffic for the next hour
    next_hour = (current_hour + 1)
    predicted_traffic = model.predict(np.array([[next_hour]]))

    # Perform network optimization based on predicted traffic
    # In a real scenario, this would involve adjusting network parameters, routing, or scaling resources.
    # For simplicity, we'll just print the prediction and sleep for an hour.
    # Creating a standard message for logging output
    message = f"[Predicted Bandwidth Utilization: {((predicted_traffic[0]/bandwidth)*100):.3f}%] - Predicted Network Traffic for {next_hour}:00: {predicted_traffic[0]:.3f} Mbps "
    
    # Setting logging levels base off bandwidth percentages
    if predicted_traffic[0] < (bandwidth * .7):
        # Log as info, if under 70%
        logging.info(msg=message)
    elif predicted_traffic[0] >= (bandwidth * .7) and predicted_traffic[0] < (bandwidth * .9):
        # Log as warning, if over 70% and under 90%
        logging.warning(msg=message)
    elif predicted_traffic[0] >= (bandwidth * .9) and predicted_traffic[0] < (bandwidth * 1):
        # Log as critical, if over 90% and under 100%
        logging.critical(msg=message)
    else:
        # Log as error, if 100% or higher
        logging.error(msg=f'[Blocking Prediction] - {message}')
        
    current_hour = current_hour + 1
    time.sleep(1)  # Simulate sleep for an hour 
    
