import numpy as np
from sklearn.ensemble import IsolationForest
import time

# Simulated network traffic data (you would replace this with real data)
# In this example, we generate random traffic values.
network_traffic = np.random.normal(100, 20, 1000)

# Create an isolation forest model for anomaly detection
model = IsolationForest(contamination=0.05)  # 5% of data is considered anomalous

# Continuously monitor network traffic for anomalies
while True:
    # Simulate real-time network traffic data (replace with actual data)
    new_traffic = np.random.normal(100, 20, 1)

    # Predict if the new data point is anomalous
    anomaly_score = model.fit_predict(new_traffic.reshape(-1, 1))

    if anomaly_score[0] == -1:
        print(f"Suspicious network activity detected: {new_traffic[0]}")
        # Implement a response mechanism (e.g., block IP, alert admin) here

    # Sleep for a short period before the next observation
    time.sleep(1)
