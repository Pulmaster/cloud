from flask import Flask
from flask_cors import CORS
from flask import render_template,request, redirect, url_for, flash
from flask import session
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

# Models:
from models.UsuarioModel import UsuarioModel

# Entities:
from models.entities.Usuario import Usuario
from config import config

# Routes
from routes import Evento

app = Flask(__name__)

csrf = CSRFProtect()
WTF_CSRF_ENABLED = False
login_manager_app = LoginManager(app)

CORS(app, resources={"*":{"origins":"*"}})

def page_not_found(error):
    return "<h1>No existe la pagina</h1>",404

@login_manager_app.user_loader
def load_user(id):
    return UsuarioModel.get_by_id(id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/eventos')
def index2():
    return render_template('eventos.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = Usuario(0, request.form['correoUsuario'], request.form['contrasenaUsuario'])
        logged_user = UsuarioModel.login(user)
        print(logged_user)
        if logged_user != None:
            if logged_user.contrasenaUsuario:
                print(logged_user.idUsuario)
                login_user(logged_user)
                return render_template('eventos.html',name=logged_user.idUsuario)
            else:
                flash("Contraseña Invalida...")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"



if __name__=='__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    WTF_CSRF_ENABLED = False
    # Blueprints
    app.register_blueprint(Evento.main,url_prefix='/api/eventos')
    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()