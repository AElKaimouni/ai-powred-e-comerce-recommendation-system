# AI-Powered Recommendation System

## Overview
This project implements an AI-powered recommendation system using Python and Flask. The system recommends products to users based on their browsing and purchase history. It utilizes the TF-IDF algorithm for content-based recommendation and computes user profiles to personalize recommendations.

The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/ahmedaliraja/e-commerece-sales-data-2023-24). It includes e-commerce sales data for the years 2023-24. Please note that we manually modified some sales data to increase sales for specific clients with IDs ranging from 1 to 10. This modification was done to test and evaluate the effectiveness of our recommendation model.

## Files

1. **recommendation_engine:**
   - **__main__.py:** Entry point of the recommendation engine. Defines the main logic for recommending products to users.
   - **data_preprocessing.py:** Contains functions for reading and preprocessing data.
   - **product_recommendation.py:** Contains functions for recommending products based on TF-IDF and cosine similarity.
   - **user_profile.py:** Contains functions for generating user profiles based on browsing history.

2. **server.py:**
   - Implements a Flask server to expose recommendation endpoints via HTTP.
   - Defines routes `/recommend` and `/user/<int:user_id>` to recommend products to users.
   - Handles incoming requests, extracts user ID and count parameters, and returns recommended products as JSON responses.

## How to Run

1. Ensure you have Python installed on your system.
2. Install Flask and pandas libraries using pip: `pip install flask pandas`.
3. Run the Flask server by executing `server.py`: `python server.py`.
4. send HTTP GET requests to `http://localhost:5000/user/<user_id>?count=<count>` to get recommendations for a specific user.

## API Documentation

### Description
This API provides endpoints to recommend products to users based on their browsing and purchase history. It utilizes an AI-powered recommendation system implemented in Python and Flask. The recommendation engine analyzes user behavior and product data to generate personalized recommendations for each user.

### Endpoints

#### GET /user/<user_id>
- **Description:** Retrieves product recommendations for a specific user.
- **Parameters:**
  - `user_id` (integer, required): The unique identifier of the user for whom recommendations are requested.
  - `count` (integer, optional): The number of product recommendations to return (default: 1). Maximum value allowed is 20.
- **Response:**
  - Status Code: 200 OK
  - Body: JSON object containing an array of recommended products.

### Error Handling

- **400 Bad Request:** Returned if The `count` parameter exceeds the maximum value of 20.
- **404 Not Found:** Returned if the specified `user_id` does not exist.

## Dependencies

- Python 3.x
- Flask
- pandas
- scikit-learn (for TF-IDF vectorization)

## Note

- This is a basic recommendation system and can be extended with additional features such as collaborative filtering, user feedback integration, and performance optimization.
- Ensure that the CSV files in the `data` directory are correctly formatted and contain valid data for the recommendation system to function properly.
