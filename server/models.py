from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db


# contains definitions of tables and associated schema constructs
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
})

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)


class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False)
    in_stock = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String, nullable=False)
    

    # 1 item has many reviews: 1-to-many relationship between items and reviews tables
    reviews = db.relationship('Review', back_populates='item', cascade='all')

    # Items and customers Many-to-Many relationship: The items review customers
    customers = association_proxy('reviews', 'customer', creator = lambda c: Review(customer = c))

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, nullable=False, unique=True)

    # 1 customer has many reviews: 1-to-many relationship between customers and reviews tables
    reviews = db.relationship('Review', back_populates='customer', cascade='all')


    @validates('first_name', 'last_name')
    def validate_columns(self, attr, value):
        if (not isinstance(value, str)) or len(value) < 2:
            raise ValueError(f"{attr} must be a string that is at least 2 characters long!")
        return value
    
    @validates('username')
    def validate_username(self, attr, value):
        if (not isinstance(value, str)) or len(value) < 3:
            raise ValueError(f"{attr} must be at least 3 characters long!")
        return value
    
    @validates('password')
    def validate_password(self, attr, value):
        if (not isinstance(value, str)) or len(value) < 7:
            raise ValueError(f"{attr} must contain a special character and be at least 7 characters long!")
        elif not any(char in value for char in '!@#$%^&*_'):
            raise ValueError(f'{attr} must contain a special character!')
        return value
        



class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    date_reviewed = db.Column(db.Date, nullable=False)
    text = db.Column(db.String, nullable=False)

    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    # A review belongs to an item: 1-to-many relationship between item and reviews tables
    item = db.relationship('Item', back_populates='reviews')

    # A review belongs to a customer: 1-to-many relationship between customers and reviews tables
    customer = db.relationship('Customer', back_populates='reviews')

    @validates('text')
    def validate_columns(self, attr, value):
        if (not isinstance(value, str)) or len(value) < 3:
            raise ValueError(f"{attr} must be a string that is at least 3 characters long!")
        return value