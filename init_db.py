"""
Database Initialization Script
Author: Ankit Rajput
Description: Initialize PostgreSQL database with required tables
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/restaurant_db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(500))
    available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class InventoryItem(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String(20), nullable=False)
    reorder_level = Column(Float, nullable=False)
    cost_per_unit = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    table_number = Column(Integer)
    status = Column(String(20), nullable=False)
    total_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime)

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    name = Column(String(100), nullable=False)
    ingredients = Column(String(1000), nullable=False)
    total_cost = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_database():
    """Initialize database with tables"""
    print('\n' + '='*60)
    print('🗄️  Database Initialization')
    print('👨‍💻 Author: Ankit Rajput')
    print('='*60 + '\n')

    try:
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        print('✅ Database tables created successfully!')
        print('='*60 + '\n')
    except Exception as e:
        print(f'❌ Error creating database: {str(e)}')
        print('='*60 + '\n')

if __name__ == '__main__':
    init_database()
