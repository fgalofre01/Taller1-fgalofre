from utils.db import db

class Usuario(db.Model):
     __tablename__ = 'usuarios'
    
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(150), nullable = False)
     password = db.Column(db.String(150), nullable = False)
 
    
    
     def __init__(self, username, password):
        self.username = username
        self.password = password
    