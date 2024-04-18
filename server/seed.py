#!/usr/bin/env python3
from random import randint, choice as rc
from models import db, Item, Customer, Review
from app import app
import datetime

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        
        db.create_all()
        
        Item.query.delete()
        Customer.query.delete()
        Review.query.delete()

        item1 = Item(name="Duffle1", price= 399.99, image="drewnix/Development/code/phase-4/phase-4-project/LeatherSite/client/public/images/duffle.png", in_stock= 3, category= 'Accessory')
        item2 = Item(name="Apron1", price= 99.99, image="drewnix/Development/code/phase-4/phase-4-project/LeatherSite/client/public/images/apron.png", in_stock= 3, category= 'Accessory')
        item3 = Item(name="Purse1", price= 149.99, image="drewnix/Development/code/phase-4/phase-4-project/LeatherSite/client/public/images/purse.png", in_stock= 3, category= 'Accessory')
        item4 = Item(name="Boot1", price= 249.99, image="drewnix/Development/code/phase-4/phase-4-project/LeatherSite/client/public/images/boot.jpg", in_stock= 10, category= 'Clothing')
        
        



        customer1 = Customer(first_name="Drew", last_name="Hairston", username="dch528", password='123456!', email_address='dch528@gmail.com')

        customer2 = Customer(first_name="Liz", last_name="Catoe", username="eccatoe2517", password='123456!', email_address='eccatoe2517@gmail.com')

        customer3 = Customer(first_name="Bob", last_name="Robertson", username="bobbert123", password='123456!', email_address='doublebob@gmail.com')

        customers = [customer1, customer2, customer3]
        
    # Initialize  the Review object by passing in the the Objects 'Item' and 'Customer' as objects not as integers'
        review1 = Review(date_reviewed=datetime.date(year=2024, month=4, day=14), text= "Great boots for casual wear and work.", item=item4, customer=customer1)

        review2 = Review(date_reviewed=datetime.date(year=2024, month=4, day=14), text="Super sturdy! Great as carry-on luggage.", item=item1, customer=customer2)

        review3 = Review(date_reviewed=datetime.date(year=2024, month=4, day=14), text="So cute! I wish it had an enclosure.", item=item3, customer=customer3)

        review4 = Review(date_reviewed=datetime.date(year=2024, month=4, day=14), text="Great style and very sturdy, but leather is heavy for a kitchen apron.", item=item2, customer=customer1)


      
        
        db.session.add_all([item1, item2, item3, item4])
        db.session.add_all([customer1, customer2, customer3])
        db.session.add_all([review1, review2, review3, review4])
        
     
        db.session.commit()
        print("🌱 Items, Customers, and Reviews successfully seeded! 🌱")