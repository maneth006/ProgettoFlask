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


#rotta principale
@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all() #COMMENTA
    return render_template('index.html', lista = lista_spesa)
    #visualizza

@app.route('/aggiungi', methods=['POST'])#usando il metodo post aggiungiamo un elemento alla lista
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        nuovo_elemento = ListaSpesa(elemento=elemento) #COMMENTA
        db.session.add(nuovo_elemento) #COMMENTA
        db.session.commit() #COMMENTA
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])#usando il metodo post rimuoviamo un elemento dalla lista
def rimuovi(indice):
    elemento = ListaSpesa.query.get_or_404(indice) #COMMENTA
    db.session.delete(elemento) #COMMENTA
    db.session.commit() #COMMENTA
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota():
    ListaSpesa.query.delete() #COMMENTA ???
    db.session.commit() #COMMENTA ???
    return redirect(url_for('home'))

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)