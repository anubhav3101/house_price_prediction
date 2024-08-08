import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

# Load the dataset
file_path = os.path.join(os.path.dirname(__file__), 'data', 'housing_data.csv')
data = pd.read_csv(file_path)

# Preprocess the dataset (adjust based on your data)
data = data[['bedrooms', 'bathrooms', 'sqft_living', 'price']]

X = data[['bedrooms', 'bathrooms', 'sqft_living']]
y = data['price']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
pickle.dump(model, open('model.pkl', 'wb'))
