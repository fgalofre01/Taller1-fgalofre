from flask import render_template, jsonify
from models.cuidadores import Cuidador
from models.perros import Perros
from utils.db import db

def principal_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")
        #return jsonify({"mensaje": "Tablas creadas"}), 201

    @app.route("/mostrar_cuidadores", methods=["GET"])
    def listar_cuidadores():
        cuidadores = Cuidador.query.all()
        lista_cuidadores = [{"id": cuidador.id, "nombre": cuidador.nombre, "telefono": cuidador.telefono} for cuidador in cuidadores]
        return jsonify(lista_cuidadores)

    @app.route("/mostrar_perritos", methods=["GET"])
    def listar_perros():
        perros = Perros.query.all()
        lista_perros = [{"id": perro.id, "nombre": perro.nombre, "raza": perro.raza, "edad": perro.edad, "peso": perro.peso, "id_cuidador": perro.id_cuidador} for perro in perros]
        return jsonify(lista_perros)

    @app.route("/contar_perros")
    def contar_perros():
        cantidad_perros = Perros.query.filter_by(nombre="Lassie").count()
        return render_template("contar_perros.html", cantidad_perros=cantidad_perros)

    @app.route("/asignar_perros_mario")
    def asignar_perros_a_mario():
        cuidador_mario = Cuidador.query.filter_by(nombre="Mario").first()
        if not cuidador_mario:
            return "Empleado Mario no encontrado", 404
        perros_ligeros = Perros.query.filter(Perros.peso < 3).all()
        for perro in perros_ligeros:
            perro.id_cuidador = cuidador_mario.id 
        db.session.commit()
        return render_template("perros_asignados.html", nombre_cuidador="Mario", perros = perros_ligeros)

