import requests

def optimize_content_delivery(user_features):
    # Make a request to the ML API for prediction
    response = requests.post('http://localhost:5000/predict', json=user_features)
    prediction = response.json()['prediction']

    # Use the prediction to route the content request
    optimized_server = choose_optimal_server(prediction)
    return optimized_server
