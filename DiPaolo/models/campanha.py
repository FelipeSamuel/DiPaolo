from DiPaolo import db
from DiPaolo import manager

class Campanha(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    ativa = db.Column(db.Boolean)

    titulo = db.Column(db.String(255))
    descricao = db.Column(db.Text)

    data_inicio = db.Column(db.DateTime)
    data_fim = db.Column(db.DateTime)

manager.create_api(Campanha, methods=['GET', 'POST', 'PUT', 'DELETE'])