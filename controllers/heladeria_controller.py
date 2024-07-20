from flask import  render_template
from app import app
from models.heladeria import Heladeria




@app.route("/ListarProductos")
def main():
    heladeria = Heladeria()
    productos = heladeria.productos
    return render_template("index.html", productos = productos)
    

@app.route("/vender/<idproductos>")
def confir(idproductos):
    heladeria = Heladeria()
    resultado = heladeria.vender(idproductos)
    print(resultado)
    return render_template("venta.html", resultado = resultado)