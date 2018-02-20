from DiPaolo import db
from DiPaolo import manager

from DiPaolo.models.cliente import Cliente
from DiPaolo.models.funcionario import Funcionario

class ClienteAvaliaFuncionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    data_avaliacao = db.Column(db.DateTime)

    nota_atendimento = db.Column(db.Integer)
    comentario = db.Column(db.Text)

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    cliente = db.relationship('Cliente',  backref=db.backref('cliente_avaliacao', lazy=True))

    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=True)
    funcionario = db.relationship('Funcionario',  backref=db.backref('funcionario_avaliacao', lazy=True))

manager.create_api(ClienteAvaliaFuncionario, methods=['GET', 'POST','PUT', 'DELETE'])

