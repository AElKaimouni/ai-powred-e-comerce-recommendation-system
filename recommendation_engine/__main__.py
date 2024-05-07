from recommendation_engine.user_profile import generate_user_profile
from recommendation_engine.product_recommendation import recommend_products
import math

def recommend_user(user_id, products_count):
    user_profile = generate_user_profile(user_id) # generate user profile
    products = [] # init the products list

    for product in user_profile: # add products to our list based on each product in user profile
        products = products + recommend_products(product[0], math.ceil(product[1] * products_count))
    
    return products[:products_count]