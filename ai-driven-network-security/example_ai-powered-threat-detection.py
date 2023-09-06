# Anomaly detection example
import numpy as np
from sklearn.ensemble import IsolationForest

# Generate sample network traffic data
np.random.seed(0)
data = np.random.randn(100, 2)

# Train an isolation forest model for anomaly detection
model = IsolationForest(contamination=0.05)
model.fit(data)

# Detect anomalies
anomalies = model.predict(data)
print("Anomalies detected:", np.sum(anomalies == -1))
