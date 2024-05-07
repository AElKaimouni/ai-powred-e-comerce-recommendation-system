from flask import Flask, request, jsonify
from recommendation_model import recommend_user

app = Flask(__name__)


@app.route('/recommend', methods=['POST'])
def recommend_products():
    data = request.get_json()  # Get JSON data from the request body
    user_id = data.get('user_id')
    count = data.get('count')

    return jsonify(recommend_user(int(user_id), int(count)))

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    count = request.args.get('count', default=1, type=int)  # Get 'count' parameter from URL query string

    return jsonify(recommend_user(int(user_id), count))

if __name__ == '__main__':
    app.run(debug=True)