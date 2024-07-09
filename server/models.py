from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
  __tablename__ = 'users'
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(), unique=True, nullable=False)
  email = db.Column(db.String(), unique=True, nullable=False)
  password = db.Column(db.String(), nullable=False)
  
  reviews = db.relationship('Review', back_populates = 'user')
  travel_guides =db.association_proxy('reviews', 'travel_guide')
  
class Destination(db.Model, SerializerMixin):
  __tablename__ = 'destinations'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  location = db.Column(db.String(), nullable=False)
  image = db.Column(db.String(), nullable=False)
  
  reviews = db.relationship('Review', back_populates = 'destination')
  users = db.association_proxy('reviews', 'user')
  
class Review(db.Model, SerializerMixin):
  __tablename__ = 'reviews'
  
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'), nullable=False)
  rating = db.Column(db.Integer, nullable=False)
  comment = db.Column(db.String(), nullable=False)
  
  user = db.relationship('User', back_populates = 'reviews')
  destination = db.relationship('Travel_Guide', back_populates = 'reviews')