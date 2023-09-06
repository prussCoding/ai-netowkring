from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load and preprocess the dataset
X, y = preprocess_data(user_data)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest regression model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


