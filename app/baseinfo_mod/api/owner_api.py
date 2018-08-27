from app.baseinfo_mod.model.owner import Owner

def create_owner_blueprint(api_manager):    
    owner_api = api_manager.create_api_blueprint(Owner, methods = ['GET','POST'])
    api_manager.app.register_blueprint(owner_api, url_prefix = '/api')