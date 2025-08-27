import uuid

from sqlalchemy import select

from models import session_maker, User, Product, Order, Ticket

class BuyProductException(Exception):
    pass

def create_user(username: str, password: str) -> User:
    with session_maker() as session:
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

def get_user(username: str, password: str) -> User | None:
    with session_maker() as session:
        user = session.query(User).filter(User.username == username, User.password == password).first()
        return user

def get_all_products() -> list[Product]:
    with session_maker() as session:
        query = select(Product).where(Product.count > 0).order_by(Product.id.desc())
        products = session.execute(query).scalars().all()
        return list(products)

def buy_product(user_id: int, product_id: int, count: int) -> Order:
    with session_maker() as session:
        user = session.get(User, user_id)
        if user is None:
            raise BuyProductException("Пользователь не найден!")
        product = session.get(Product, product_id)
        if product is None:
            raise BuyProductException("Продукт не найден!")
        if product.count < count:
            raise BuyProductException("Недостаточно товара!")
        total_price = product.cost * count
        if user.points < total_price:
            raise BuyProductException("Недостаточно поинтов!")
        user.points -= total_price
        product.count -= count
        order = Order(user_id=user_id, product_id=product_id, count=count)
        session.add(order)
        session.commit()
        session.refresh(order)
        return order

def use_ticket(user_id: int, ticket_uuid: str):
    with session_maker() as session:
        ticket = session.query(Ticket).filter(Ticket.uuid == ticket_uuid, Ticket.available == True).first()
        if ticket is None:
            raise ValueError("Тикет недействителен!")
        ticket.available = False
        ticket.user_id = user_id
        user = session.get(User, user_id)
        user.points += 20
        session.commit()

def get_profile_points(user_id: int) -> int:
    with session_maker() as session:
        user = session.get(User, user_id)
        return user.points if user else 0

def get_profile_orders(user_id: int) -> list:
    with session_maker() as session:
        query = select(Product.name, Order.count).join(Product).filter(Order.user_id == user_id)
        orders = session.execute(query).all()
        return orders

def generate_tickets(num_tickets: int = 5):
    with session_maker() as session:
        for _ in range(num_tickets):
            ticket_uuid = str(uuid.uuid4())
            ticket = Ticket(uuid=ticket_uuid)
            session.add(ticket)
        session.commit()

def add_product(name: str, cost: int, count: int, seller_id: int):
    with session_maker() as session:
        product = Product(name=name, cost=cost, count=count, seller_id=seller_id)
        session.add(product)
        session.commit()