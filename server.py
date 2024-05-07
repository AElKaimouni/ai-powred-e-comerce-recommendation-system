from flask import Flask, request, abort, jsonify
from recommendation_engine.__main__ import recommend_user
from recommendation_engine.data_preprocessing import customers_df


app = Flask(__name__)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    count = request.args.get('count', default=1, type=int)  # Get 'count' parameter from URL query string

    if count > 20:
        abort(400, 'the max amount of recommendation is 20!') # Abort the request count greater that 20
    if user_id not in customers_df['Customer ID'].values:
        abort(404, "the specified user is not exist.")  # Abort the request with 404 error if user not found

    return jsonify(recommend_user(int(user_id), count))

if __name__ == '__main__':
    app.run(debug=True)