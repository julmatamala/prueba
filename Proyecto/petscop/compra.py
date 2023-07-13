class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self, producto):
        id = str(producto.id)
        cantidad_solicitada = 1  # Modifica esto según cómo se determine la cantidad solicitada
        
        if id not in self.carrito.keys():
            if cantidad_solicitada > producto.cantidad:
                # La cantidad solicitada supera la cantidad disponible del producto
                # Aquí puedes lanzar una excepción, mostrar un mensaje de error, etc.
                return

            self.carrito[id] = {
                "producto_id": producto.id, 
                "producto_nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": cantidad_solicitada
            }
        else:
            if self.carrito[id]["cantidad"] + cantidad_solicitada > producto.cantidad:
                # La cantidad solicitada más la cantidad existente en el carrito
                # supera la cantidad disponible del producto
                # Aquí puedes lanzar una excepción, mostrar un mensaje de error, etc.
                return

            self.carrito[id]["cantidad"] += cantidad_solicitada
            self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

        
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()
    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True