from DiPaolo import db
from DiPaolo import manager

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    usuario = db.Column(db.String(45))
    senha = db.Column(db.String(45))
    permissoes = db.Column(db.Text)

    tipo = db.Column(db.Boolean) # 0 - Cliente, 1 - Funcionario

manager.create_api(Login, methods=['POST', 'PUT','DELETE', 'GET'])


