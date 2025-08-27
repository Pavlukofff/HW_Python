from models import User
from services import create_user, get_user, get_all_products, buy_product, BuyProductException, use_ticket, get_profile_points, get_profile_orders

welcome_text = """
===============================================
    === Добро пожаловать в "Не магазин" ===
"""

menu_non_registered = """
    Доступные действия:
    > Товары
    > Зарегистрироваться
    > Войти
"""

menu_registered = """
    Доступные действия:
    > Товары
    > Купить
    > Профиль
    > Тикет
    > Выход
"""

class ExitException(Exception):
    pass

class Menu:
    def __init__(self):
        self._user: User | None = None

    def get_commands_text(self) -> str:
        text = "\nДля взаимодействия используйте команды:\n"
        if self._user is None:
            text += menu_non_registered
        else:
            text += menu_registered
        return text

    def welcome(self) -> str:
        return welcome_text + self.get_commands_text()

    def process_action(self, action: str) -> str:
        action = action.lower().strip()
        if action == "товары":
            return process_show_products_action()
        elif action.startswith("купить"):
            if self._user is None or self._user.id is None:
                return "Для покупки товара необходимо войти в аккаунт"
            return process_buy_product_action(action, self._user.id)
        elif action.startswith("тикет"):
            if self._user is None or self._user.id is None:
                return "Для добавления тикета необходимо войти в аккаунт"
            return process_ticket_action(action, self._user.id)
        elif action == "зарегистрироваться":
            self._user = process_register_action()
            return "Регистрация прошла успешно" if self._user is not None else "Регистрация не удалась"
        elif action == "войти":
            self._user = process_login_action()
            return "Вход выполнен" if self._user is not None else "Вход не выполнен"
        elif action == "профиль" and self._user is not None and self._user.id is not None:
            return process_profile_action(self._user.id)
        elif action == "выход" and self._user is not None:
            raise ExitException()
        else:
            return "Неверная команда!"

    def run(self):
        print(self.welcome())
        while True:
            try:
                action = input("Введите команду: ")
                print(self.process_action(action))
            except ExitException:
                print("До свидания!")
                break
            print(self.get_commands_text())

def process_register_action() -> User | None:
    username = input("Введите имя пользователя: ")
    if User.is_exist(username):
        print("Пользователь с таким именем уже существует")
        return None
    while True:
        password1 = input("Введите пароль: ")
        password2 = input("Повторите пароль: ")
        if password1 == password2:
            break
        print("Пароли не совпадают")
    return create_user(username, password1)

def process_login_action() -> User | None:
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    user = get_user(username, password)
    if user is None:
        print("Неверный логин или пароль")
        return None
    return user

def process_show_products_action() -> str:
    products = get_all_products()
    if not products:
        return "Нет доступных товаров."
    max_id = max(len("ID"), max(len(str(p.id)) for p in products)) + 2
    max_cost = max(len("Стоимость"), max(len(str(p.cost)) for p in products)) + 2
    max_count = max(len("Кол-во"), max(len(str(p.count)) for p in products)) + 2
    max_name = max(len("Название"), max(len(p.name) for p in products)) + 2

    text = f" {'ID':<{max_id}} | {'Стоимость':<{max_cost}} | {'Кол-во':<{max_count}} | {'Название':<{max_name}}\n"
    text += "-" * (max_id + max_cost + max_count + max_name + 3) + "\n"
    for p in products:
        text += f" {p.id:<{max_id}} | {p.cost:<{max_cost}} | {p.count:<{max_count}} | {p.name:<{max_name}}\n"
    return text

def process_buy_product_action(action: str, user_id: int) -> str:
    action_parts = action.split()
    if len(action_parts) != 3:
        return "Неверный формат команды, введите 'купить <id> <количество>'"
    if not action_parts[1].isdigit() or not action_parts[2].isdigit():
        return "Неверный формат, '<id> и <количество>' должны быть числами"
    try:
        order = buy_product(user_id, int(action_parts[1]), int(action_parts[2]))
    except BuyProductException as exc:
        return str(exc)
    return f"Покупка товара №{order.product_id} успешно оформлена, ID заказа: {order.id}"

def process_ticket_action(action: str, user_id: int) -> str:
    action_parts = action.split()
    if len(action_parts) != 2:
        return "Неверный формат команды, введите 'тикет <uuid>'"
    ticket_uuid = action_parts[1]
    try:
        use_ticket(user_id, ticket_uuid)
        return "Тикет использован! Получено 20 поинтов!"
    except ValueError as exc:
        return str(exc)

def process_profile_action(user_id: int) -> str:
    points = get_profile_points(user_id)
    orders = get_profile_orders(user_id)
    text = f"Поинты: {points}\nЗаказы:\n"
    if not orders:
        text += "Нет заказов."
    else:
        for name, count in orders:
            text += f"{name}: {count}\n"
    return text