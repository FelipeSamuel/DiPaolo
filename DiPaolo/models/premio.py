from DiPaolo import db
from DiPaolo import manager

class Premio(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    ativo = db.Column(db.Boolean)

    nome = db.Column(db.String(100))
    fotos = db.Column(db.Text)
    descricao = db.Column(db.Text)

    nivel = db.Column(db.Integer) # nivel do premio. de 1 a 5

manager.create_api(Premio, methods=['GET', 'POST', 'PUT', 'DELETE'])