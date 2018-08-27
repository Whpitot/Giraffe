from app.baseinfo_mod.model.warehouse import Warehouse

def create_warehouse_blueprint(api_manager):    
    warehouse_api = api_manager.create_api_blueprint(Warehouse, methods = ['GET','POST'])
    api_manager.app.register_blueprint(warehouse_api, url_prefix = '/api')