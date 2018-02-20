from DiPaolo import db
from DiPaolo import manager
from enum import Enum

class TIPO_MENSAGEM(Enum):
    EMAIL = "email"

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    tipo_mensagem = db.Column(db.Enum(TIPO_MENSAGEM))

    assunto = db.Column(db.String(255))
    mensagem = db.Column(db.Text)
    origem = db.Column(db.String(255))
    destinatarios = db.Column(db.Text)
    anexos = db.Column(db.Text)

    data_envio = db.Column(db.DateTime)
    enviado = db.Column(db.Boolean)

manager.create_api(Mensagem, methods=['POST', 'GET', 'PUT', 'DELETE'])