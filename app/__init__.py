from flask import Flask
from flask.ext.mail import Mail

application = Flask(__name__)

application.config.update(dict(
    MAIL_SERVER = "smtp.googlemail.com",
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "yalenus.js@gmail.com",
    MAIL_PASSWORD = "bancho138614",
))

mail = Mail(application)

from app import views
