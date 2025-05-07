from marshmallow import Schema, fields

class InfoPokemonSchema(Schema):
    id = fields.Integer(dump_only=True)
    pokemon_name = fields.String(required=True)
    move = fields.String(required=True)

