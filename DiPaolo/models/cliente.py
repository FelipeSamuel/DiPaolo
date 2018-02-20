from DiPaolo import db
from DiPaolo import manager

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    ativo = db.Column(db.Boolean)

    nome = db.Column(db.String(100))
    foto = db.Column(db.String(100))
    sobrenome = db.Column(db.String(100))
    data_nascimento = db.Column(db.DateTime)

    data_cadastro = db.Column(db.DateTime)

    logradouro = db.Column(db.String(255))
    numero = db.Column(db.String(10))
    bairro = db.Column(db.String(100))
    complemento = db.Column(db.String(255))
    cep = db.Column(db.String(20))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(30))

    usuario = db.Column(db.String(45))
    senha = db.Column(db.String(45))

    telefone = db.Column(db.String(20))
    celular = db.Column(db.String(20))
    site = db.Column(db.String(100))
    email = db.Column(db.String(100))

manager.create_api(Cliente, methods=['GET', 'POST', 'PATCH', 'DELETE'], allow_patch_many=True)