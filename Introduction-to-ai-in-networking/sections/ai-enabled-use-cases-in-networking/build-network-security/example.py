import numpy as np
from sklearn.ensemble import IsolationForest
import time
import logging

# Set logging basic configuration
logging.basicConfig(format='%(levelname)s:  %(message)s', level=logging.DEBUG)

# Set Normal Distribution Variables
mean = 100
standard_deviation = 20
size = 1000

# Set Baseline Traffic 
network_traffic = np.random.normal(mean, standard_deviation, size)

# Create an isolation forest model for anomaly detection and fit baseline traffic
model = IsolationForest(contamination=0.05)  # 5% of data is considered anomalous
model.fit(network_traffic.reshape(-1, 1))


# Continuously monitor network traffic for anomalies
while True:
    # Simulate real-time network traffic data (replace with actual data)
    new_traffic = np.random.normal(mean, standard_deviation, 1)
    
    # Create standard message for logging
    message = f'network activity detected: {new_traffic[0]}'
 
    # Predict if the new data point is anomalous
    anomaly_score = model.predict(new_traffic.reshape(-1, 1))
    
    if anomaly_score[0] == -1:
        logging.warning(f"Suspicious {message}")
        # Implement a response mechanism (e.g., block IP, alert admin) here
    else: 
        logging.info(f"Accepted {message}")
    
    # Sleep for a short period before the next observation
    time.sleep(1)
