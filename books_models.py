import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()
class Publisher(Base):
    __tablename__ = 'Publisher'
    publisherID = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length=80), unique = True, nullable=False)
    def __str__(self):
        return f'{self.name} {self.publisherID}'


class Book(Base):
    __tablename__ = 'Book'
    bookID = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=120), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('Publisher.publisherID'), nullable=False)

    publisher = relationship(Publisher, backref = 'book')
    def __str__(self):
        return f'Book {self.bookID} {self.title} {self.id_publisher}'


class Shop(Base):
    __tablename__ = 'Shop'
    shopID = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length=60), nullable=False)
    def __str__(self):
        return f'Shop {self.shopID} {self.name}'

class Stock(Base):
    __tablename__ = 'Stock'
    stockID = sq.Column(sq.Integer, primary_key = True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('Book.bookID'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('Shop.shopID'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')

    def __str__(self):
        return f'Stock {self.stockID} - {self.count} {self.id_book} {self.id_shop}'

class Sale(Base):
    __tablename__ = 'Sale'
    saleID = sq.Column(sq.Integer, primary_key = True)
    price = sq.Column(sq.Float, nullable = False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock=sq.Column(sq.Integer, sq.ForeignKey('Stock.stockID'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref='sale')

def create_tables(engine):
    Base.metadata.create_all(engine)