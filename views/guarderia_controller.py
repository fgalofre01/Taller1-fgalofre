from flask import render_template, jsonify, request, redirect, flash, url_for   
from models.cuidadores import Cuidador
from models.perros import Perros
from models.usuario import users
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from utils.db import db

def principal_routes(app):

    # Configuración de flask-login
    login_manager = LoginManager(app)
    login_manager.login_view = 'login'
        
    @app.route('/')
    def index():
     return render_template('index.html')

    @app.route('/login', methods =["GET", "POST"])
    def login():
        if request.method == 'GET':
            return render_template("login.html")
        else:
            username = request.form['nombre']
            password = request.form['password']
            logout_user()
            
            for user in users:
                if user.username == username and user.password == password:
                    login_user(user)
                    flash('Inicio de sesion exitoso','success')
                    if user.is_admin:
                        return redirect(url_for('admin_dashboard'))
                    else:
                        return redirect(url_for('dashboard'))
            else:
                flash('Usuario o password incorrectos','danger')
                return redirect(url_for('login'))

    @login_manager.user_loader
    def load_user(user):
        for user in users:
            if user.id == int(user.id):
               return user
        return None

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Has cerrado sesión', 'danger')
        return redirect(url_for('login'))

    @app.route('/dashboard')
    @login_required
    def dashboard():
            return render_template('dashboard.html')
    
    @app.route('/admin_dashboard')
    @login_required
    def admin_dashboard():
        if current_user.is_admin:
           return render_template('admin_dashboard.html', name = current_user.username)
        return render_template('login.html')


    @app.route('/mostrar_cuidadores')
    def mostrar_cuidadores():
         if current_user.is_admin:
            cuidadores = Cuidador.query.all()
            return render_template('mostrar_cuidadores.html', cuidadores = cuidadores)
         return render_template('login.html')
    
    @app.route('/mostrar_perritos')
    def mostrar_perritos():
        if current_user.is_admin:
            perritos = Perros.query.all()
            return render_template('mostrar_perritos.html', perritos = perritos)
        return render_template('login.html')
    
    @app.route("/contar_perros")
    def contar_perros():
        if current_user.is_admin:
            cantidad_perros = Perros.query.filter_by(nombre="Lassie").count()
            return render_template("contar_perros.html", cantidad_perros = cantidad_perros)
        return render_template('login.html')
    
    @app.route("/asignar_perros_mario")
    def asignar_perros_a_mario():
        if current_user.is_admin:
            cuidador_mario = Cuidador.query.filter_by(nombre="Mario").first()
            if not cuidador_mario:
                return "Empleado Mario no encontrado", 404
            perros_ligeros = Perros.query.filter(Perros.peso < 3).all()
            for perro in perros_ligeros:
                perro.id_cuidador = cuidador_mario.id 
            db.session.commit()
            return render_template("perros_asignados.html", nombre_cuidador = "Mario", perros = perros_ligeros)
        return render_template('login.html')

