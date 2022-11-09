from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://*******@cluster0.w7vjg0p.mongodb.net/test'
)

db = client.tokendb


def add_user(token, color, col_value, price, price_value):
    db.users.insert_one({
        'token': token,
        color: col_value,
        price: price_value,
    })


def check_user(token):
    user = db.users.find_one({'token': token})
    if user:
        return user
    return False


def get_all_col():
    rows = db.users.find({})
    result = {}
    for row in rows:
        color = row['btn_color']
        result.setdefault(color, 0)
        result[color] += 1
    return result


def get_all_price():
    rows = db.users.find({})
    result = {}
    for row in rows:
        price = row['price']
        result.setdefault(price, 0)
        result[price] += 1
    return result
