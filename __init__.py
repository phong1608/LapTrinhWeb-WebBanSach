from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
import os
from flask_login import LoginManager,login_user

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///website.db"
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()

login_manager.__init__(app)
login_manager.login_view = 'login'
login_manager.needs_refresh_message_category = 'danger'
login_manager.login_message = u"Bạn cần đăng nhập"
