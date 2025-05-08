from marshmallow import Schema, fields

class InfoPokemonSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, data_key="pokemon")
    move = fields.String(required=True)
    type = fields.String(required=True)
    generation = fields.String(required=True)

