from flask import Flask, render_template
#render_template: collegare file HTML.

#inizializza l'app Flask
app = Flask(__name__)

#rotta principale
@app.route('/')
def home():
    return render_template('index.html')

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)