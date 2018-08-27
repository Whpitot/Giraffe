# coding:utf-8

from marshmallow import fields
from app.baseinfo_mod.shcema.base_entity_schema import BaseEntitySchema

class CompanySchema(BaseEntitySchema):
    code = fields.Str(required = True)
    name_cn = fields.Str(required = True)
    name_cn_long = fields.Str()
    address = fields.Str()
    tel = fields.Str()
    contact = fields.Str()
      
