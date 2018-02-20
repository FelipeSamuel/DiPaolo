from DiPaolo import db
from DiPaolo import manager

class Configuracao(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    ativa = db.Column(db.Boolean)

    chave = db.Column(db.String(255))
    valor = db.Column(db.String(255))

manager.create_api(Configuracao, methods=['GET', 'POST', 'PUT', 'DELETE'])