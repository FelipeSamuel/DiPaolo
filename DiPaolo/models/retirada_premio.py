from DiPaolo import db
from DiPaolo import manager

from DiPaolo.models.cliente import Cliente

class RetiradaPremio(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    quantidade_visitas = db.Column(db.Integer)
    data_retirada = db.Column(db.DateTime)

    codigo_premio = db.Column(db.Integer)
    premio = db.Column(db.String(100))

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    cliente = db.relationship('Cliente',  backref=db.backref('cliente_retirada', lazy=True))

manager.create_api(RetiradaPremio, methods=['GET', 'POST', 'PUT', 'DELETE'])