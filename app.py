from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, ListaSpesa
#render_template: collegare file HTML.

#inizializza l'app Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

lista_Spesa = []
#rotta principale
@app.route('/')
def home():
    return render_template('index.html', lista_Spesa = lista_Spesa)
    #visualizza

@app.route('/aggiungi', methods=['POST'])#usando il metodo post aggiungiamo un elemento alla lista
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista_Spesa.append(elemento)
    return redirect(url_for('home'))
@app.route('/rimuovi/<int:indice>', methods=['POST'])#usando il metodo post rimuoviamo un elemento dalla lista
def rimuovi(indice):
    if 0 <= indice < len(lista_Spesa):
        lista_Spesa.pop(indice)
    return redirect(url_for('home'))

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)