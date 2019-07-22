# -*-coding:utf8-*-

from db import db
from app.baseinfo_mod.model.base_entity import BaseEntity

class Product(BaseEntity, db.Model):
    __tablename__ = 'product'    

    code = db.Column(db.String(50))
    name_cn = db.Column(db.String(30))
    name_en = db.Column(db.String(30))
    barcode = db.Column(db.String(50))
    category_id = db.Column(db.Integer)
    category_code = db.Column(db.String(30))
    category_name = db.Column(db.String(30))
    brand = db.Column(db.String(50))
    item_no = db.Column(db.String(30))
    size = db.Column(db.String(10))
    unit = db.Column(db.String(10))
    price = db.Column(db.Float)
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    high = db.Column(db.Float)    
    volume = db.Column(db.Float)
    weight = db.Column(db.Float)
