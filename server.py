from flask_app import app

from flask_app.controllers import servicios, usuarios, estados, ordenes, clientes

if __name__ == "__main__":
    app.run(debug=True)
