import pandas as pd
from recommendation_engine.data_preprocessing import products_df, sales_df

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