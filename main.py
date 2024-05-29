from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def index():
    return "hola_mundo:]"

@app.route("/chau")
def goodbye():
    return "chau"



app.run()
