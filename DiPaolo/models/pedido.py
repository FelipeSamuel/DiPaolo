from DiPaolo import manager
from DiPaolo import db
from enum import Enum

from DiPaolo.models.cliente import Cliente
from DiPaolo.models.funcionario import Funcionario


class STATUS(Enum):
    ABERTO = "Aberto"
    CANCELADO = "Cancelado"
    VISUALIZADO = "Visualizado"
    EM_ESPERA = "Em Espera"
    EM_ATENDIMENTO = "Em atendimento"
    SAIU_PARA_ENTREGA = "Saiu para entrega"
    FINALIZADO = "Finalizado"

class FORMA_PAGAMENTO(Enum):
    A_VISTA = "A vista"

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.Enum(STATUS))

    valor_total = db.Column(db.Float)

    data_emissao = db.Column(db.DateTime)
    data_fechamento = db.Column(db.DateTime)

    forma_pagamento = db.Column(db.Enum(FORMA_PAGAMENTO))
    observacao = db.Column(db.Text)

    nota_tempo = db.Column(db.Integer)
    nota_qualidade = db.Column(db.Integer)
    comentario_nota = db.Column(db.Text)

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    cliente = db.relationship('Cliente',  backref=db.backref('cliente_pedido', lazy=True))

    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=True)
    funcionario = db.relationship('Funcionario',  backref=db.backref('funcionario_pedido', lazy=True))



manager.create_api(Pedido, methods=['GET', 'POST', 'PUT', 'DELETE'])