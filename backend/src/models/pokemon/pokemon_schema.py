from marshmallow import Schema, fields

class PokemonSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    type = fields.String(required=True)
    generation = fields.String(required=True)
