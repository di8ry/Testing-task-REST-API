import json


def add_user(token, color, col_value, price, price_value):
    with open('result.json', 'r') as file:
        data = json.load(file)
        data.update({
            token: {
                color: col_value,
                price: price_value,
            }})
    with open('result.json', 'w') as file:
        json.dump(data, file, indent=4)


def check_user(token):
    with open('result.json') as file:
        user = json.load(file)
        if token in user:
            return user
        return False


def get_all_col():
    with open('result.json') as file:
        file_ = json.load(file)
        result = {}
        for row in file_.values():
            print(row)
            color = row.get('btn_color')
            price = row.get('price')
            result.setdefault(color, 0)
            result[color] += 1
            result.setdefault(price, 0)
            result[price] += 1
        return result
