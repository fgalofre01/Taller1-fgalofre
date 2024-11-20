from utils.db import db

class Perros(db.Model):
    __tablename__ = 'perros'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable = False)
    raza = db.Column(db.String(50), nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    peso = db.Column(db.Float, nullable = False)
    id_cuidador = db.Column(db.Integer, db.ForeignKey('cuidadores.id'), nullable=False)
    
    def __init__(self, nombre, raza, edad, peso, id_cuidador):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.id_cuidador = id_cuidador
        self._peso = peso
    
