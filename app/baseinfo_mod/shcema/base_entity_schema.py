from marshmallow import Schema, fields

class BaseEntitySchema(Schema):
    id = fields.Int(dump_only = True)  #dump_only 只能被serialization，而不能被deserialization
    creator = fields.Str()
    create_at = fields.DateTime()
    modifier = fields.Str()
    modify_at = fields.DateTime()

    company_id = fields.Int()
    company_code = fields.Str()
    company_name = fields.Str()
    warehouse_id = fields.Int()
    warehouse_code =  fields.Str()
    warehouse_name = fields.Str()
    owner_id = fields.Int()
    owner_code = fields.Str()
    owner_name = fields.Str()