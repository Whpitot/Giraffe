# -*-coding:utf8-*-
import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_cors import CORS
from config import config
from db import db

from app.api.Customer_api import customer_view
from app.api.Product_api import product_view
from app.api.InstallOrder_api import installOrder_view
# from app.api.Entity_api


def create_app():    
    app = Flask(__name__)   # 第一个参数是模块或者包的名字，参数是必须的
    CORS(app)
    print os.environ.get('MODE')
    if os.environ.get('MODE')=='TEST_SQLITE':
        app.config.from_object(config['development_sqlite_disk']) #config是一个字典  
    else:
        app.config.from_object(config['development_mysql'])    
    db.app = app
    db.init_app(app)

    app.add_url_rule('/customers/', defaults={'pk': None}, view_func=customer_view, methods=['GET',])
    app.add_url_rule('/customers', view_func=customer_view, methods=['POST',])
    app.add_url_rule('/customers/<int:pk>', view_func=customer_view, methods=['GET', 'PUT', 'DELETE'])

    app.add_url_rule('/products/',defaults={'pk':None}, view_func=product_view,methods=['GET',])
    app.add_url_rule('/products',view_func=product_view,methods=['POST',])
    app.add_url_rule('/products/<int:pk>',view_func=product_view,methods=['GET','PUT','DELETE'])

    app.add_url_rule('/installOrders/',defaults={'pk':None}, view_func=installOrder_view,methods=['GET',])
    app.add_url_rule('/installOrders',view_func=installOrder_view,methods=['POST',])
    app.add_url_rule('/installOrders/<int:pk>',view_func=installOrder_view,methods=['GET','PUT','DELETE'])    
     

    return app    

 