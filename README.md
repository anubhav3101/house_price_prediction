House Price Prediction Web Application


Welcome to the House Price Prediction web application project. This application is designed to predict house prices based on input features such as the number of bedrooms, bathrooms, and square footage. The application uses a machine learning model to make these predictions and is built using Flask, a lightweight web framework for Python.

Project Structure


The project is organized to ensure clarity and ease of navigation. The root directory contains the main application files (app.py and model.py), along with directories for HTML templates, CSS files, and the dataset. Specifically, app.py is the main Flask application file that handles the web server and routes, while model.py is responsible for training and saving the machine learning model. The templates directory houses the HTML templates, the static directory contains the CSS files, and the data directory includes the dataset file used for model training.

Setup Instructions


To set up and run the project, follow these steps:

Clone the Repository: Begin by cloning the repository to your local machine using the command git clone <your-repo-url>. Navigate to the project directory with cd house_price_prediction.
Install Dependencies: Install the necessary libraries by running the command pip install Flask pandas scikit-learn. This will install Flask for the web application and pandas and scikit-learn for data manipulation and machine learning, respectively.
Train the Model: Execute the model training script by running python model.py. This script will load the dataset, preprocess it, train a Linear Regression model, and save the model as model.pkl in the root directory.
Run the Flask Application: Start the Flask application by running python app.py. Once the server is running, open your web browser and navigate to http://127.0.0.1:5000/ to access the application.
Usage
The web application provides a user-friendly form where users can input house features, including the number of bedrooms, bathrooms, and total square footage. After entering the details, users can click the "Predict" button to get an estimated house price based on the input features. The predicted price is then displayed on the web page.

Screenshots
To help you understand the application's functionality, here are some screenshots:

Form Input: This screenshot shows the form where users can input house features.

![image](https://github.com/user-attachments/assets/9b45840f-88a3-4c8b-aa2f-2b64921699fd)


Prediction Output: This screenshot displays the predicted house price based on the user's input.

![image](https://github.com/user-attachments/assets/ab39dbb4-3bd2-4cc8-94db-d540e7ce1e9a)

