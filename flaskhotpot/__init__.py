from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor

import os


app = Flask(__name__)
app.config["SECRET_KEY"] = "4ac60774b647c110518817f4bd6bde54"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["CKEDITOR_FILE_UPLOADER"] = "upload"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["UPLOADED_PATH"] = os.path.join(basedir, "uploads")


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
ckeditor = CKEditor(app)


from flaskhotpot import routes
