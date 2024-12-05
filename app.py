from utils.inventory import list_items, add_item
from utils.users import get_user_info

def main():
    print("Система управління магазином одягу")
    print("1. Переглянути список товарів")
    print("2. Додати новий товар")
    print("3. Переглянути інформацію про користувача")
    choice = input("Оберіть дію (1-3): ")

    if choice == "1":
        list_items()
    elif choice == "2":
        name = input("Введіть назву товару: ")
        quantity = int(input("Введіть кількість: "))
        price = float(input("Введіть ціну: "))
        add_item(name, quantity, price)
    elif choice == "3":
        username = input("Введіть ім'я користувача: ")
        get_user_info(username)
    else:
        print("Невірний вибір.")

if __name__ == "__main__":
    main()