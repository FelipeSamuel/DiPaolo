from DiPaolo import app
from flask import request
from flask import jsonify

from DiPaolo import mail
from flask_mail import Message

from DiPaolo import db

from DiPaolo.models.mensagem import Mensagem, TIPO_MENSAGEM
import datetime

@app.route('/api/email', methods=['POST'])
def enviar_email():

    assunto = request.json['assunto'] if 'assunto' in request.json else None
    email_origem = request.json['origem'] if 'origem' in request.json else None
    destinatarios = request.json['destinatarios'] if 'origem' in request.json else None
    mensagem = request.json['mensagem'] if 'mensagem' in request.json else None

    try:
        msg = Message(assunto, sender=email_origem, recipients=destinatarios)
        msg.body = mensagem
        mail.send(msg)

        return jsonify({
                "sucesso": True, 
                 "erro": None,
                 "assunto": assunto,
                 "origem": email_origem,
                 "destinatarios": destinatarios,
                 "mensagem": mensagem
                 })
    except Exception as e:
        return jsonify({
                "sucesso": True, 
                 "erro": str(e),
                 "assunto": assunto,
                 "origem": email_origem,
                 "destinatarios": destinatarios,
                 "mensagem": mensagem
                 })