from db import db

class Ingredientes(db.Model):
    idingredientes = db.Column(db.Integer, primary_key = True)
    nombreIngrediente = db.Column(db.String(45), nullable = False)
    numeroCalorias = db.Column(db.Integer, nullable = False)
    precioIngrediente = db.Column(db.Integer, nullable = False)
    inventario = db.Column(db.Float, nullable = False)
    vegetariano = db.Column(db.Boolean, nullable = False)
    tipoIngrediente = db.Column(db.Boolean, nullable = False)
    sabor  = db.Column(db.String(45), nullable = True)

    def act_ingrediente(self,cantidad):
        self.inventario = cantidad
        db.session.commit()

    def ingredientesano(self):
        if self.vegetariano and self.numeroCalorias < 100:
            return True
        else:
            return False
    
    def abastecer(self)->None:
        self.inventario =+ 5
        db.session.commit

    def renovar_inentario(self):
        if self.tipoIngrediente == False:
            self.inventario = 0
            db.session.commit()

    

    
        