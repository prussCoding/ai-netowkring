import numpy as np

# Generate synthetic network traffic data
np.random.seed(0)
X = np.random.rand(100, 1)  # Features (e.g., time of day)
y = 50 + 30 * X + np.random.randn(100, 1) * 10  # Target (e.g., network latency)
