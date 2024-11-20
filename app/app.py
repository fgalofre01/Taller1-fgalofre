from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from utils.db import db, init_db
from views.principal_controller import principal_routes
#from models.perros import Perros
import os

load_dotenv()
app = Flask(__name__)

#DB_STRING_CONNECTION = os.getenv('DB_STRING_CONNECTION')
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
#app.config["SQLALCHEMY_DATABASE_URI"]= 'mysql+pymysql://root:3M3Cw365aB2OXc5C@localhost:3306/tablas' 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)#SQLAlchemy(app)
init_db(app)

principal_routes(app)

if __name__ == "__main__":
    app.run(debug=True)