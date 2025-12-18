from flask import Flask
from categoria_controller import categoria_bp
from cliente_controller import cliente_bp

app = Flask(__name__)

app.register_blueprint(categoria_bp)
app.register_blueprint(cliente_bp)

@app.route('/')
def home():

    return {"status":"API rodando🚀"}
