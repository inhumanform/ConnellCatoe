#!/usr/bin/env python3

# Standard library imports


# Remote library imports
from flask import Flask, make_response, request, session, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS



# Local imports
from config import app, db, api
# Add your model imports
from models import db, Item, Customer, Review

app = Flask(__name__)

# configure a database connection to the local file examples.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leathersite.db'

# disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

api = Api(app)


    
# Views go here! 

class AllItems(Resource):

    def get(self):
        items = Item.query.all()
        response_body = [item.to_dict(only=('id', 'name', 'price', 'image', 'in_stock')) for item in items]
        return make_response(response_body, 200)

api.add_resource(AllItems, '/items' )


class ItemByID(Resource):
    def get(self, id):
        item = db.session.get(Item, id)

        if item: 
            response_body = item.to_dict(rules=('-reviews.item', '-reviews.customer'))

            response_body['customers'] = [customer.to_dict(only=('id', 'first_name', 'last_name', 'username')) for customer in item.customers]
            
            return make_response(response_body, 200)
        
        else:
            response_body = {
                'error': "Item Not Found"
            }
            return make_response(response_body, 404)
        

api.add_resource(ItemByID, '/items/<int:id>')

#  AllCustomers needs attention

class AllCustomers(Resource):

    def get(self):
        customers = Customer.query.all()
        customer_list_with_dictionaries = [customer.to_dict(only=('id', 'first_name', 'last_name', 'username')) for customer in customers]
        return make_response(customer_list_with_dictionaries, 200)
    
    def post(self):
        try:
            new_customer = Customer(first_name=request.json.get('first_name'), last_name=request.json.get('last_name'), username=request.json.get('username'))
            db.session.add(new_customer)
            db.session.commit()
            response_body = new_customer.to_dict(only=('id', 'first_name', 'last_name', 'username'))
            return make_response(response_body, 201)
        except:
            response_body = {
                "error": "Customer's first name and last name cannot be the same, and first name and last name must be at least 2 characters long! Customer must have a username!"
            }
            return make_response(response_body, 400)
    
api.add_resource(AllCustomers, '/customers')

class CustomerByID(Resource):

    def get(self, id):
        customer = db.session.get(Customer, id)

        if customer:
            response_body = customer.to_dict(rules=('-reviews.item', '-reviews.customer'))

            # Add in the association proxy data (The customer's items)
            response_body['items'] = [item.to_dict(only=('id', 'name', 'image')) for item in list(set(customer.items.items))]

            return make_response(response_body, 200)
        
        else:
            response_body = {
                'error': "Customer Not Found"
            }
            return make_response(response_body, 404)
        
    def patch(self, id):
        customer = db.session.get(Customer, id)

        if customer:
            try:
                for attr in request.json:
                    setattr(customer, attr, request.json[attr])
                
                db.session.commit()
                response_body = customer.to_dict(only=('id', 'first_name', 'last_name', 'username'))
                return make_response(response_body, 200)
            except:
                response_body = {
                    "error": "Customer's first name and last name cannot be the same, and first name and last name must be at least 3 characters long! Customer must have a username!"
                }
                return make_response(response_body, 400)
        
        else:
            response_body = {
                'error': "Customer Not Found"
            }
            return make_response(response_body, 404)
         
    def delete(self, id):
        customer = db.session.get(Customer, id)

        if customer:
            db.session.delete(customer)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
        
        else:
            response_body = {
                'error': "Customer Not Found"
            }
            return make_response(response_body, 404)

api.add_resource(CustomerByID, '/customers/<int:id>')

# AllReviews needs attention

class AllReviews(Resource):
    
    def get(self):
        reviews = Review.query.all()
        review_list_with_dictionaries = [review.to_dict(rules=('-item.reviews', '-customer.reviews')) for review in reviews]
        return make_response(review_list_with_dictionaries, 200)
    
    def post(self):
        try:
            new_review = Review(rating=request.json.get('rating'), text=request.json.get('text'), item_id=request.json.get('item_id'), customer_id=request.json.get('customer_id'))
            db.session.add(new_review)
            db.session.commit()
            response_body = new_review.to_dict(rules=('-item.reviews', '-customer.reviews'))
            return make_response(response_body, 201)
        except ValueError as value_error:
            value_error_string = str(value_error)
            response_body = {
                "error": value_error_string
            }
            return make_response(response_body, 400)
    
api.add_resource(AllReviews, '/reviews')

class ReviewByID(Resource):

    def get(self, id):
        review = db.session.get(Review, id)

        if review:
            response_body = review.to_dict(rules=('-item.reviews', '-customer.reviews'))
            return make_response(response_body, 200)
        
        else:
            response_body = {
                "error": "Review Not Found"
            }
            return make_response(response_body, 404)
        
    def patch(self, id):
        review = db.session.get(Review, id)

        if review:
            try:
                for attr in request.json:
                    setattr(review, attr, request.json.get(attr))
                
                db.session.commit()
                response_body = review.to_dict(rules=('-item.reviews', '-customer.reviews'))
                return make_response(response_body, 200)
            
            except ValueError as value_error:
                value_error_string = str(value_error)
                response_body = {
                    "error": value_error_string
                }
                return make_response(response_body, 400)
        
        else:
            response_body = {
                "error": "Review Not Found"
            }
            return make_response(response_body, 404)
        
    def delete(self, id):
        review = db.session.get(Review, id)

        if review:
            db.session.delete(review)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
        
        else:
            response_body = {
                "error": "Review Not Found"
            }
            return make_response(response_body, 404)

api.add_resource(ReviewByID, '/reviews/<int:id>')
 

@app.route('/')
def index():
    return '<h1>Leather Site</h1>'


if __name__ == '__main__':
        app.run(port=5555, debug=True)

