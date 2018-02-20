from DiPaolo import db
from DiPaolo import manager

from DiPaolo.models.pedido import Pedido
from DiPaolo.models.item_cardapio import ItemCardapio

class PedidoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    quantidade = db.Column(db.Float)

    valor_unitario = db.Column(db.Float)
    valor_desconto = db.Column(db.Float)
    valor_total = db.Column(db.Float)

    observacao = db.Column(db.Text)

    item_id = db.Column(db.Integer, db.ForeignKey('item_cardapio.id'), nullable=False)
    item = db.relationship('ItemCardapio',  backref=db.backref('cardapio_item', lazy=True))

    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    pedido = db.relationship('Pedido',  backref=db.backref('pedido_item', lazy=True))


manager.create_api(PedidoItem, methods=['GET', 'POST', 'PUT', 'DELETE'])