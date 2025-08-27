from menu import Menu
from models import Base, engine, session_maker, Seller
from services import generate_tickets, add_product

def create_tables():
    try:
        Base.metadata.create_all(engine)
        print("Таблицы успешно созданы.")
    except Exception as e:
        print(f"Ошибка при создании таблиц: {e}")

if __name__ == "__main__":
    create_tables()

    # generate_tickets(num_tickets=5)

    # with session_maker() as session:
    #     seller = Seller(company="TestCompany")
    #     session.add(seller)
    #     session.commit()
    #     add_product("Яблоко", 10, 5, 1)  # seller_id = 1
    #     add_product("Апельсин", 20, 3, 1)  # seller_id = 1

    menu = Menu()
    menu.run()