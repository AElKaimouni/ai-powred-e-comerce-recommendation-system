from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from recommendation_engine.data_preprocessing import products_df

# generate tags columns that contain important data about each product
products_df['tags'] = products_df['Product Name'] + ' ' + products_df['Category'] + ' ' + products_df['About Product']

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the product descriptions
tfidf_matrix = tfidf_vectorizer.fit_transform(products_df['tags'])

# Compute cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def recommend_products(product_id, products_count):
    idx = products_df[products_df['Uniqe Id'] == product_id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx])) # Get similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) # Sort scores
    sim_scores = sim_scores[1:products_count + 1] # Get top similar products
    product_indices = [i[0] for i in sim_scores] # Get indices of recommended products
    return products_df.iloc[product_indices].to_dict(orient='records') # Return recommended products