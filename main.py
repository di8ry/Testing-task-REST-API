from flask import Flask, request, jsonify
from random import choice, randint, choices
from fake_headers import Headers
from local_json import add_user, check_user, get_all_col


app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def color():
    headers = Headers(headers=True).generate()
    request.headers = headers
    token = randint(1000, 9999)
    request.headers['Device-token'] = token
    user = check_user(token)
    if user:
        return user
    color_ = choice(app.config['COLOR']['btn_color'])
    price = choices(app.config['COLOR']['price'], weights=[0.75, 0.1, 0.05, 0.1])[0]
    add_user(token, 'btn_color', color_, 'price', price)
    return jsonify(price, color_)


@app.route('/stats')
def stats():
    return jsonify(get_all_col())


if __name__ == '__main__':
    app.run(debug=True)
