from DiPaolo import manager
from DiPaolo import db

class ItemCardapio(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    em_estoque = db.Column(db.Boolean)
    ativo = db.Column(db.Boolean)

    titulo = db.Column(db.String(255))
    descricao = db.Column(db.Text)
    modo_preparo = db.Column(db.Text)
    ingredientes = db.Column(db.Text)

    valor = db.Column(db.Float)
    valor_desconto = db.Column(db.Float)
    fotos = db.Column(db.Text) # Urls separadas por ;
    capa = db.Column(db.String(100))

manager.create_api(ItemCardapio, methods=['GET', 'POST', 'PUT', 'DELETE'])