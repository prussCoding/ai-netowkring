# Time series forecasting example
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Generate synthetic network performance data
np.random.seed(0)
time_points = np.arange(1, 101)
network_traffic = 50 + 2 * time_points + np.random.normal(0, 10, 100)

# Train a Holt-Winters forecasting model
model = ExponentialSmoothing(network_traffic, seasonal='add', seasonal_periods=12)
model_fit = model.fit()

# Make predictions for the next 5 time points
forecast = model_fit.forecast(steps=5)
print("Network traffic forecast for the next 5 time points:", forecast)
