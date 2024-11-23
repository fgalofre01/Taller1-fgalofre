from utils.db import db

class Cuidador(db.Model):
     __tablename__ = 'cuidadores'
    
     id = db.Column(db.Integer, primary_key=True)
     nombre = db.Column(db.String(150), nullable = False)
     telefono = db.Column(db.String(50), nullable = False)
     perros = db.relationship('Perros', backref='cuidador', lazy=True)
    
    
     def __init__(self, nombre: str, telefono: str) -> None :
        self.nombre = nombre
        self.telefono = telefono
    