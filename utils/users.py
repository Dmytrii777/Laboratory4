def get_user_info(username):
    users = {
        "admin": {"role": "Адміністратор", "email": "admin@store.com"},
        "manager": {"role": "Менеджер", "email": "manager@store.com"},
    }

    user = users.get(username)
    if user:
        print(f"Інформація про користувача:")
        print(f"- Роль: {user['role']}")
        print(f"- Email: {user['email']}")
    else:
        print("Користувача не знайдено.")
