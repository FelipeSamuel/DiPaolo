from DiPaolo import app
import os
import json

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://samukajo_root:codigoefotografia12345@felipesamuel.com/samukajobs_dipaolo'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/di_paolo'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Configuracao do cliente de email
def config_email():
    with open(os.getcwd()+'\\DiPaolo\\config\\email.json', 'r') as myfile:
        return json.loads(myfile.read())

json = config_email()

app.config.update(
	MAIL_SERVER= json['smtp'],
	MAIL_PORT= json['porta'],
	MAIL_USE_SSL= json['ssl'],
	MAIL_USERNAME = json['usuario'],
	MAIL_PASSWORD = json['senha']
	)
