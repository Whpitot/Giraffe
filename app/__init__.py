# -*-coding:utf8-*-
import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from config import config
from config import config
from db import db

from flask_restless import APIManager
from app.baseinfo_mod.api.company_api import create_company_blueprint
from app.baseinfo_mod.api.owner_api import create_owner_blueprint
from app.baseinfo_mod.api.warehouse_api import create_warehouse_blueprint

def create_app():    
    app = Flask(__name__)   # 第一个参数是模块或者包的名字，参数是必须的
    print os.environ.get('MODE')
    if os.environ.get('MODE')=='TEST_SQLITE':
        app.config.from_object(config['development_sqlite_disk']) #config是一个字典  
    else:
        app.config.from_object(config['development_mysql'])    
    db.app = app
    db.init_app(app)

    # flask-restless
    restless_api_manager = APIManager(app, flask_sqlalchemy_db = db)
    create_company_blueprint(restless_api_manager)
    create_owner_blueprint(restless_api_manager)
    create_warehouse_blueprint(restless_api_manager)

    return app    
