from app.baseinfo_mod.model.company import Company

def create_company_blueprint(api_manager):
    # get http://127.0.0.1:5000/api/company
    # {
    #     "num_results": 1,
    #     "objects": [
    #         {
    #             "address": null,
    #             "code": null,
    #             "company_code": "1",
    #             "company_id": 1,
    #             "company_name": "1",
    #             "contact": null,
    #             "create_at": null,
    #             "creator": "12",
    #             "id": 1,
    #             "modifier": "12",
    #             "modify_at": null,
    #             "name_cn": null,
    #             "name_cn_long": null,
    #             "owner_code": null,
    #             "owner_id": null,
    #             "owner_name": null,
    #             "tel": null,
    #             "warehouse_code": "1",
    #             "warehouse_id": 1,
    #             "warehouse_name": "1"
    #         }
    #     ],
    #     "page": 1,
    #     "total_pages": 1
    # }

    # post http://127.0.0.1:5000/api/company
    # {
    #     "address": "jslfjsl",
    #     "code": null,
    #     "company_code": "1",
    #     "company_id": 1,
    #     "company_name": "1",
    #     "contact": null,
    #     "create_at": "2018-08-23T11:14:34",
    #     "creator": "12",
    #     "id": 2,
    #     "modifier": "12",
    #     "modify_at": "2018-08-23T11:14:34",
    #     "name_cn": null,
    #     "name_cn_long": null,
    #     "owner_code": null,
    #     "owner_id": null,
    #     "owner_name": null,
    #     "tel": null,
    #     "warehouse_code": "1",
    #     "warehouse_id": 1,
    #     "warehouse_name": "1"
    # }
    
    company_api = api_manager.create_api_blueprint(Company, methods = ['GET','POST'])
    api_manager.app.register_blueprint(company_api, url_prefix = '/api')

