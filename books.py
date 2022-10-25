from books_models import create_tables, Publisher, Stock, Sale, Shop, Book
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import psycopg2
from pprint import pprint


with open('Books_pass.txt') as f:
    DSN = f.read()
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

Publisher1 = Publisher(name ='Pearson')
Publisher2 = Publisher(name = 'Microsoft Press')
Publisher3 = Publisher(name ='No starch press')

Book1 = Book(title = 'Programming Python, 4th Edition', id_publisher = '42')
Book2 = Book(title = 'Learning Python, 4th Edition', id_publisher = '43')
Book3 = Book(title = 'Natural Language Processing with Python', id_publisher = '44')
Book4 = Book(title = 'Hacking: The Art of Exploitation', id_publisher = '43')
Book5 = Book(title = 'Modern Operating Systems', id_publisher = '42')

Shop1 = Shop(name = 'Labirint')
Shop2 = Shop(name = 'OZON')
Shop3 = Shop(name = 'Amazon')


Stock1 = Stock(id_book = '10', id_shop = '7', count = '15')
Stock2 = Stock(id_book = '9', id_shop = '8', count = '30')
Stock3 = Stock(id_book = '8', id_shop = '7', count = '1')
Stock4 = Stock(id_book = '7', id_shop = '8', count = '40')
Stock5 = Stock(id_book = '6', id_shop = '9', count = '18')
Stock6 = Stock(id_book = '7', id_shop = '9', count = '20')
Stock7 = Stock(id_book = '8', id_shop = '8', count = '30')
Stock8 = Stock(id_book = '9', id_shop = '7', count = '40')

# session.add_all([])
# session.commit()
publisher_input = input('Введите имя издателя: ')
for a in session.query(Shop.name, Publisher.name).distinct(Shop.name).join(Stock.shop).join(Book).join(Publisher).filter(Publisher.name==publisher_input).all():
    print(a[0])

session.close()