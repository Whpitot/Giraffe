# -*-coding:utf8-*-

from db import db

class Warehouse(db.Model):
    __tablename__ = 'warehouse'

    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    creator = db.Column(db.String(50))
    create_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    modifier = db.Column(db.String(50))
    modify_at = db.Column(db.DateTime, default = db.func.current_timestamp())

    company_id = db.Column(db.Integer)
    company_code = db.Column(db.String(50))
    company_name = db.Column(db.String(50))
    
    code = db.Column(db.String(50))
    name_cn = db.Column(db.String(30))
    name_cn_long = db.Column(db.String(50))
    address = db.Column(db.String(50))
    tel = db.Column(db.String(20))
    contact = db.Column(db.String(10))
