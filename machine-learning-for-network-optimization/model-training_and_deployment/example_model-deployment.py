def predict_latency(input_features):
    # Normalize input features if necessary
    # input_features = (input_features - mean) / std

    # Perform prediction using the trained model
    predicted_latency = model.predict(input_features)

    # Return the predicted latency
    return predicted_latency[0][0]
