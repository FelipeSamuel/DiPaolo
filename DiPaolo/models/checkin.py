from DiPaolo import db
from DiPaolo import manager

from DiPaolo.models.cliente import Cliente

class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    valida = db.Column(db.Boolean) # Caso verdadeira, pode ser contabilizada na hora da retirada do premio, caso falso, sera ignorada

    data_visita = db.Column(db.DateTime)

    ignora_feedback = db.Column(db.Boolean)
    nota_atendimento = db.Column(db.Integer)
    nota_tempo = db.Column(db.Integer) # tempo de espera
    nota_qualidade = db.Column(db.Integer) # qualidade da refeicao

    comentario = db.Column(db.Text)

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    cliente = db.relationship('Cliente',  backref=db.backref('cliente_visita', lazy=True))


manager.create_api(CheckIn, methods=['GET', 'POST', 'PUT', 'DELETE'])