import json

DATABASE_PATH = "database.json"

def load_data():
    try:
        with open(DATABASE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"items": []}

def save_data(data):
    with open(DATABASE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def list_items():
    data = load_data()
    print("Список товарів:")
    for item in data["items"]:
        print(f"- {item['name']}: {item['quantity']} шт, {item['price']} грн")

def add_item(name, quantity, price):
    data = load_data()
    data["items"].append({"name": name, "quantity": quantity, "price": price})
    save_data(data)
    print(f"Товар {name} додано успішно!")
