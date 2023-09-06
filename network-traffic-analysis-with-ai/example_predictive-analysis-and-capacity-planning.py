# Network traffic forecasting and capacity planning example
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Generate synthetic network traffic data
np.random.seed(0)
time_points = np.arange(1, 101)
network_traffic = 50 + 2 * time_points + np.random.normal(0, 10, 100)

# Train a Holt-Winters forecasting model
model = ExponentialSmoothing(network_traffic, seasonal='add', seasonal_periods=12)
model_fit = model.fit()

# Make predictions for the next 10 time points
forecast = model_fit.forecast(steps=10)

# Visualize historical and forecasted network traffic
plt.plot(time_points, network_traffic, label='Historical Traffic')
plt.plot(np.arange(101, 111), forecast, label='Forecasted Traffic', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Network Traffic')
plt.legend()
plt.show()

print("Network traffic forecast for the next 10 time points:", forecast)
