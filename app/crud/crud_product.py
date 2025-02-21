from sqlalchemy.orm import Session
from app.db import models

def get(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create(db: Session, obj_in):
    db_product = models.Product(**obj_in.dict())
    db.add(db_product)  
    db.commit()
    db.refresh(db_product)
    return db_product

def update(db: Session, db_obj, obj_in):
    db_obj_data = db_obj.__dict__
    update_data = obj_in.dict(exclude_unset=True)
    for field in db_obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product