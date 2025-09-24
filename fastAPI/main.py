from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas
from . import models
from .database import SessionLocal, engine, get_db

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CRUD Operations for Customers
# --- Create (POST) ---
@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(
        CustomerName=customer.CustomerName,
        Email=customer.Email,
        Address=customer.Address
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# --- Read All (GET) ---
@app.get("/customers/", response_model=list[schemas.Customer])
def read_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

# --- Read One (GET) ---
@app.get("/customers/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.CustomerID == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

# --- Update (PUT) ---
@app.put("/customers/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int, updated_customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.CustomerID == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    db_customer.CustomerName = updated_customer.CustomerName
    db_customer.Email = updated_customer.Email
    db_customer.Address = updated_customer.Address
    db.commit()
    db.refresh(db_customer)
    return db_customer

# --- Delete (DELETE) ---
@app.delete("/customers/{customer_id}", response_model=schemas.Customer)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.CustomerID == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    db.delete(db_customer)
    db.commit()
    return db_customer

# CRUD Operations for Products (similar structure)
# CRUD operations for the Products table

# --- Create (POST) ---
@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(
        productName = product.ProductName,
        Price = product.Price,
        VendorID = product.VendorID
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# --- Read All (GET) ---
@app.get("/products/", response_model=list[schemas.Product])
def read_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

# --- Read One (GET) ---
@app.get("/products/{procuct_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.ProductID == product_id).first()
    if db_product is None:
        raise HTTPException(status_code = 404, detail="Product not found")
    return db_product

# --- Update (PUT) ---
@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, updated_product: schemas.ProductCreate, db: Session= Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.ProductID == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.ProductName = updated_product.ProductName
    db_product.Price= updated_product.Price
    db_product.VendorID = updated_product.VendorID
    db.commit()
    db.refresh(db_product)
    return db_product

# --- Delete (DELETE) ---
@app.delete("/products/{product_id}", response_model=schemas.Product)
def  delete_product(product_id: int, db:Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.ProductID == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return db_product