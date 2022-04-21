from utils.db import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from routes.incidencias import incidencias

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db" # TODO: Pass to mysql 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # TODO: review

app.register_blueprint(incidencias)

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    print("=========================================")
    print("Test me on: http://ptin2022.github.io/A2/")
    print("=========================================")
    app.run(host="0.0.0.0")
