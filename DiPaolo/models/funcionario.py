from DiPaolo import manager
from DiPaolo import db

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    ativo = db.Column(db.Boolean)

    nome = db.Column(db.String(255))
    foto = db.Column(db.String(100))
    cargo = db.Column(db.String(255))
    data_nascimento = db.Column(db.DateTime)

    data_cadastro = db.Column(db.DateTime)

    rg = db.Column(db.String(20))
    cpf = db.Column(db.String(20))

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


manager.create_api(Funcionario, methods=['GET', 'POST', 'PUT', 'DELETE'])