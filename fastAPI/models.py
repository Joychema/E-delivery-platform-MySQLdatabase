from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from .database import Base

class Customer(Base):
    __tablename__ = "Customers"
    CustomerID = Column(Integer, primary_key=True)
    CustomerName = Column(String(100), nullable=False)
    Email = Column(String(255), unique=True, nullable=False)
    Address = Column(String(255))
    orders = relationship("Order", back_populates="customer")

class Product(Base):
    __tablename__ = "Products"
    ProductID = Column(Integer, primary_key=True)
    ProductName = Column(String(255), nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)
    VendorID = Column(Integer)
    order_items = relationship("OrderItem", back_populates="product")