from DiPaolo import db
from DiPaolo import manager

class Slide(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    ativo = db.Column(db.Boolean)

    descricao = db.Column(db.Text)
    foto = db.Column(db.String(100))
    acao = db.Column(db.Text)

manager.create_api(Slide, methods=['GET', 'POST', 'PUT', 'DELETE'])