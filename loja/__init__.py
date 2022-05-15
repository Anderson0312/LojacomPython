
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads
import os
from flask_login import LoginManager
from flask_msearch import Search


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhaloja.db'
app.config['SECRET_KEY'] ='dsfgedbhef1234'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

search = Search()
search.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='clienteLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message=u'Fazer o login primeiro'



from loja.admin import rotas
from loja.produtos import rotas
from loja.carrinho import carrinhos
from loja.clientes import rotas