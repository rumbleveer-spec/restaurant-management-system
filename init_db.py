"""
Database Initialization Script
Author: Ankit Rajput
"""

from sqlalchemy import create_engine
from models import Base, User
from werkzeug.security import generate_password_hash
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/restaurant_db')

def init_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("✅ Database tables created successfully!")

    # Create default admin user
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()

    admin = User(
        username='admin',
        email='admin@restaurant.com',
        password_hash=generate_password_hash('admin123')
    )

    try:
        session.add(admin)
        session.commit()
        print("✅ Default admin user created!")
        print("   Username: admin")
        print("   Password: admin123")
    except Exception as e:
        print(f"⚠️  Admin user might already exist: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    init_database()
