# Example usage of the deployed model
input_features = np.array([[0.7]])  # Input feature (e.g., time of day)
predicted_latency = predict_latency(input_features)
print(f"Predicted Latency: {predicted_latency:.2f} ms")
