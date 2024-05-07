import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import math

# Read the CSV files into Pandas DataFrames
customers_df = pd.read_csv("data/customers.csv")
sales_df = pd.read_csv("data/sales.csv")
products_df = pd.read_csv("data/products.csv")

#validate data
sales_df = sales_df[sales_df["Interaction type"].isin(["purchase", "like", "view"])]

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the product descriptions
tfidf_matrix = tfidf_vectorizer.fit_transform(products_df['Product Name'])

# Compute cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def recommend_products(product_id, products_count):
    idx = products_df[products_df['Uniqe Id'] == product_id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx])) # Get similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) # Sort scores
    sim_scores = sim_scores[1:products_count + 1] # Get top similar products
    product_indices = [i[0] for i in sim_scores] # Get indices of recommended products
    return products_df.iloc[product_indices].to_dict(orient='records') # Return recommended products

# print(products_df.iloc[0]["Product Name"])
# print(recommend_products(0))

def generate_user_profile(user_id):
    interaction_score = { # store the factors of each interaction type
        "purchase": 3,
        "like": 2,
        "view": 1
    }

    # Get user's browsing history
    user_browsing_history = sales_df[sales_df['user id'] == user_id]
    user_browsing_history = pd.merge(user_browsing_history, products_df, left_on='product id', right_on='Uniqe Id', how='left')

    # Generate user profile based on browsing history
    user_profile = {}
    for index, product in user_browsing_history.iterrows():
        if product['product id'] not in user_profile:
            user_profile[product['product id']] = 0
        
        user_profile[product['product id']] += interaction_score[product["Interaction type"]]
        
    
    # Sort user profile by product frequency
    user_profile = sorted(user_profile.items(), key=lambda x: x[1], reverse=True)

    # limit the result to the best 10 products
    user_profile = user_profile[:10]

    # calculate the total score
    total = sum(d[1] for d in user_profile)

    # calculate the percentage of the recommandetaion for each product
    user_profile = [(d[0], d[1]/total) for d in user_profile]

    return user_profile

def recommend_user(user_id, products_count):
    user_profile = generate_user_profile(user_id) # generate user profile
    products = [] # init the products list

    for product in user_profile: # add products to our list based on each product in user profile
        products = products + recommend_products(product[0], math.ceil(product[1] * products_count))
    
    return products[:products_count]

# user_id = input("what is the user id ? ")
# count = input("how many products you wanna recommend ? ")

# for index, product in enumerate(recommend_user(int(user_id), int(count))):
#     print(str(index + 1) + "." + product)