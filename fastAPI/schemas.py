from pydantic import BaseModel

# Schema for creating a new Customer
class CustomerCreate(BaseModel):
    CustomerName: str
    Email: str
    Address: str

# Schema for displaying Customer data (Read)
class Customer(BaseModel):
    CustomerID: int
    CustomerName: str
    Email: str
    Address: str

    class Config:
        orm_mode = True

# Schema for creating a new Product
class ProductCreate(BaseModel):
    ProductName: str
    Price: float
    VendorID: int

# Schema for displaying Product data (Read)
class Product(BaseModel):
    ProductID: int
    ProductName: str
    Price: float
    VendorID: int

    class Config:
        orm_mode = True