#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User

fake = Faker()

def make_users():
    User.query.delete()
    
    users = []
    
    unique_usernames = set()

    for _ in range(20):
        username = fake.first_name()
        while username in unique_usernames:
            username = fake.first_name()
        unique_usernames.add(username)

    email = [fake.email() for _ in range(20)]
    password = [fake.password(length=8) for _ in range(20)]
    
    for i, username in enumerate(unique_usernames):
        print(f"Creating user {i + 1}: {username}, {email[i]}, {password[i]}") 
        user = User(username=username, email=email[i], password=password[i])
        print(user.username)
        users.append(user)
        print(user.username)
    
    print("Seeding users...")    
    db.session.add_all(users)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed..."),
        make_users()
        
