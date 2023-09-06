Explanation:

1. We simulate network traffic data by generating random traffic values for each hour of the day, with higher traffic during peak hours.
2. We initialize a linear regression model to predict network traffic based on the time of day.
3. The script enters a continuous loop where it:
    - Trains the model with historical data.
    - Predicts network traffic for the next hour.
    - Simulates network optimization actions based on the prediction (in a real         scenario, this would involve more complex actions).
4. The script prints the predicted traffic for the next hour and then sleeps for an hour before repeating the process.