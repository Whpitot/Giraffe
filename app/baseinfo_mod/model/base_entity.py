# -*-coding:utf8-*-

from app import db

# 基础信息字段
class BaseEntity():
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    creator = db.Column(db.String(50))
    create_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modifier = db.Column(db.String(50))
    modify_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    company_id = db.Column(db.Integer)
    company_code = db.Column(db.String(50))
    company_name = db.Column(db.String(50))
    warehouse_id = db.Column(db.Integer)
    warehouse_code =  db.Column(db.String(50))
    warehouse_name = db.Column(db.String(50))
    owner_id = db.Column(db.Integer)
    owner_code = db.Column(db.String(50))
    owner_name = db.Column(db.String(50))
