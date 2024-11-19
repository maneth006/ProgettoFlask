from flask import Flask

#inizializza l'app Flask
app = Flask(__name__)

#rotta principale
@app.route('/')
def home():
    return "Per ora funziona tutto"

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)