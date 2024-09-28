from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Ersetze das durch deinen eigenen geheimen Schlüssel
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Datenbankmodell für Benutzer
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Datenbankmodell für Gastro-Tipps
class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tip_content = db.Column(db.String(500), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Formular für die Registrierung
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=150)])
    password = PasswordField('Passwort', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Passwort bestätigen', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrieren')

# Formular für den Login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Einloggen')

# Formular für die Suche nach Gastro-Tipps
class SearchForm(FlaskForm):
    search_query = StringField('Suchbegriff', validators=[DataRequired()])
    submit = SubmitField('Suchen')

# Formular für das Hinzufügen von Gastro-Tipps
class TipForm(FlaskForm):
    tip_content = StringField('Gastro-Tipp', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Tipp hinzufügen')

# Route für die Startseite
@app.route('/')
def index():
    tips = Tip.query.all()  # Alle Tipps aus der Datenbank abrufen
    return render_template('index.html', tips=tips)

# Route für die Registrierung
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Dein Account wurde erstellt. Du kannst dich jetzt einloggen!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Route für den Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Du bist jetzt eingeloggt!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login fehlgeschlagen. Bitte überprüfe Email und Passwort.', 'danger')
    return render_template('login.html', form=form)

# Route für das Ausloggen
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Du bist jetzt ausgeloggt!', 'success')
    return redirect(url_for('index'))

# Route für die Seite zum Hinzufügen eines Gastro-Tipps
@app.route('/add_tip', methods=['GET', 'POST'])
@login_required
def add_tip():
    form = TipForm()
    if form.validate_on_submit():
        new_tip = Tip(tip_content=form.tip_content.data)
        db.session.add(new_tip)
        db.session.commit()
        flash('Dein Tipp wurde hinzugefügt!', 'success')
        return redirect(url_for('index'))
    return render_template('add_tip.html', form=form)

# Route für die Suche nach Gastro-Tipps
@app.route('/search_tip', methods=['GET', 'POST'])
def search_tip():
    form = SearchForm()
    search_results = []
    if form.validate_on_submit():
        search_query = form.search_query.data
        search_results = Tip.query.filter(Tip.tip_content.like(f'%{search_query}%')).all()
    return render_template('search_tip.html', form=form, search_results=search_results)

# Datenbanktabellen beim ersten Start erstellen
@app.before_request
def create_tables():
    if not os.path.exists('users.db'):
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
