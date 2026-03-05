from fastapi import Depends, FastAPI
from pydantic import BaseModel

from models import Product
from database import session, engine
from sqlalchemy.orm import Session
import database_model

# Pydantic model for API responses
class ProductSchema(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "welcome"

products = [
    Product(id=1, name="laptop", description="a good laptop", price=1000, quantity=10),
    Product(id=2, name="phone", description="a good phone", price=500, quantity=20),
    Product(id=3, name="tablet", description="a good tablet", price=300, quantity=15),
    Product(id=4, name="monitor", description="a good monitor", price=200, quantity=5),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(database_model.Product).count()
    if count == 0:
        for product in products:
            db.add(database_model.Product(id=product.id, name=product.name, description=product.description, price=product.price, quantity=product.quantity))
        db.commit()

init_db()

@app.get("/products", response_model=None)
def get_all_products(db: Session = Depends(get_db)):

    db_products = db.query(database_model.Product).all()
    return db_products


@app.get("/product/{id}", response_model=None)
def get_product_by_id(id:int,db: Session = Depends(get_db)):
    db_product= db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
            return db_product
    return {"error": "Product not found"}


@app.post("/product", response_model=None)
def add_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_product = database_model.Product(id=product.id, name=product.name, description=product.description, price=product.price, quantity=product.quantity)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/product", response_model=None)
def update_product(id:int ,product:ProductSchema, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product Updated"
    return {"error": "Product not found"}   

@app.delete("/product", response_model=None)
def delete_product(id:int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted"
    return {"error": "Product not found"} 