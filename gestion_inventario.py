import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self, codigo, nombre, contacto):
        self.codigo = codigo
        self.nombre = nombre
        self.contacto = contacto

    def __str__(self):
        return f"Proveedor: {self.nombre} ({self.contacto})"


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor

    def __str__(self):
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"
        return f"[{self.codigo}] {self.nombre} - {self.precio}€ ({self.stock} uds.) | {self.proveedor.__str__()}"


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero
        self.productos = []

    def cargar(self):
        try:
            with open(self.nombre_fichero, 'r') as f:
                inventario_cargado = json.load(f)
                self.productos = []
                
                for d in inventario_cargado:
                    proveedor = Proveedor(d["proveedor"]["codigo"], d["proveedor"]["nombre"], d["proveedor"]["contacto"])
                    producto = Producto(d["codigo"], 
                                        d["nombre"],
                                        d["precio"],
                                        d["stock"],
                                        proveedor)
                    self.productos.append(producto)

                print("Productos guardados correctamente")

        except FileNotFoundError:
            print("No se encontró el archivo de tareas. Comenzando con una lista vacía.")

    def guardar(self):
        # """
        # Guarda el inventario actual en el fichero JSON.
        # Convierte los objetos Producto y Proveedor en diccionarios.
        # """
        # recorrer self.productos y guardar los datos en formato JSON
        with open(self.nombre_fichero, 'w') as f:
            json.dump(self.productos, f)
                


    def anadir_producto(self, producto):
        # """
        # Añade un nuevo producto al inventario si el código no está repetido.
        # """
        # comprobar si el código ya existe y, si no, añadirlo
        if producto.codifo not in self.productos.codigo:
            self.productos.append(producto)
            print("El producto se añadio sin problema")

        print("El producto introducido ya esta registrado")

    def mostrar(self):
        # """
        # Muestra todos los productos del inventario.
        # """
        # mostrar todos los productos almacenados
        for proveedor in self.productos.proveedor:
            print(proveedor.__str__())

    def buscar(self, codigo):
        # """
        # Devuelve el producto con el código indicado, o None si no existe.
        # """
        # buscar un producto por código
        producto_buscado = [producto for producto in self.productos if codigo.lower()==self.productos.codigo.lower()]
        
        if producto_buscado:
            return producto_buscado
        return None

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        # """
        # Permite modificar los datos de un producto existente.
        # """
        # buscar el producto y actualizar sus atributos
        producto_buscado = [producto for producto in self.productos if codigo.lower()==self.productos.codigo.lower()]
        
        if producto_buscado:
            if nombre:
                self.productos.nombre = nombre
            elif precio:
                self.productos.precio = precio
            elif stock:
                self.productos.stock = stock
            else:
                print("Los datos son iguales a los anteriores")
            
        print("No hay producto con ese codigo")

    def eliminar(self, codigo):
        # """
        # Elimina un producto del inventario según su código.
        # """
        # eliminar el producto de la lista
        producto_buscado = [producto for producto in self.productos if codigo.lower()==self.productos.codigo.lower()]
        
        if producto_buscado:
            self.productos.remove(producto_buscado)
            print("Producto Eliminado")

        print("Producto no encontrado")
        

    def valor_total(self):
        # """
        # Calcula y devuelve el valor total del inventario (precio * stock).
        # """
        # devolver la suma total del valor del stock
        for p in self.productos:
            total = p.precio * p.stock
            return total

    def mostrar_por_proveedor(self, nombre_proveedor):
        # """
        # Muestra todos los productos de un proveedor determinado.
        # Si no existen productos de ese proveedor, mostrar un mensaje.
        # """
        # filtrar y mostrar los productos de un proveedor concreto
        for p in self.productos:
            if (p.proveedor.codigo.lower() == nombre_proveedor.lower()):
                print(p.__str__())


# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    objeto_inventario = Inventario("inventario.json")
    objeto_inventario.cargar()
    #  crear el objeto Inventario y llamar a los métodos según la opción elegida
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case '1':
                codigo = input("Codigo Proveedor: ")
                nombre = input("Nombre Proveedor: ")
                contacto = input("Contacto")

                codigo_producto = input("Codigo Producto:")
                nombre_producto = input("Nombre Producto:")
                try:
                    precio = float(input("Precio Producto:"))
                    stock = int(input("Stock Producto:"))
                except Exception as e:
                    print(f"Error: {e}")
                if objeto_inventario.buscar(codigo_producto):
                    print("Producto ya existente")
                else:
                    proveedor = Proveedor(codigo, nombre, contacto)
                    producto = Producto(codigo_producto, nombre_producto, precio, stock, proveedor)
                    objeto_inventario.anadir_producto(producto)

            case '2':
                objeto_inventario.mostrar()
            case '3':
                codigo = input("Codigo de Producto a buscar: ")

                producto = objeto_inventario.buscar(codigo)

                if (producto):
                    print("Producto existe")
                else:
                    print("Producto no existe")

                if producto:
                    print(f"Producto encontrado: {producto.__str__()}")
            case '4':
                codigo = input("Codigo de Producto a buscar: ")
                
                nombre = input("Nombre del Producto: ")
                try:
                    precio = float(input("Precio Producto:"))
                    stock = int(input("Stock Producto:"))
                except Exception as e:
                    print(f"Error: {e}")

                if nombre=="":
                    nombre = None
                
                objeto_inventario.modificar(codigo, nombre, precio, stock)

            case '5':
                codigo = input("Codigo de Producto: ")
                if objeto_inventario.buscar(codigo):
                    objeto_inventario.eliminar(codigo)
                else:
                    print("No existe ese producto")
            case '6':
                pass

            case '7':
                codigo ("Codigo del proveedor: ")

                objeto_inventario.mostrar_por_proveedor(codigo)
            case '8':
                objeto_inventario.guardar()
            case '_':
                print("Introduce una opcion del menu")

if __name__ == "__main__":
    main()
