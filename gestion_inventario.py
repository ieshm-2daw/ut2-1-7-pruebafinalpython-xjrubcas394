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
        return f"Nombre: {self.nombre}, Contacto: {self.contacto}"


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
        return f"[{self.codigo}] {self.nombre} - {self.precio}€ ({self.stock} uds.) | Proveedor: {self.proveedor.nombre} ({self.proveedor.contacto})"


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
                    producto = Producto(d["codigo"], 
                                        d["nombre"],
                                        d["precio"],
                                        d["stock"],
                                        d["proveedor"])
                    self.productos.append(producto)

                print("Productos guardados correctamente")

        except FileNotFoundError:
            print("No se encontró el archivo de tareas. Comenzando con una lista vacía.")
        # TODO: implementar la lectura del fichero JSON y la creación de objetos
        pass

    def guardar(self):
        # """
        # Guarda el inventario actual en el fichero JSON.
        # Convierte los objetos Producto y Proveedor en diccionarios.
        # """
        # recorrer self.productos y guardar los datos en formato JSON
        pass

    def anadir_producto(self, producto):
        # """
        # Añade un nuevo producto al inventario si el código no está repetido.
        # """
        # comprobar si el código ya existe y, si no, añadirlo
        pass

    def mostrar(self):
        # """
        # Muestra todos los productos del inventario.
        # """
        # mostrar todos los productos almacenados
        pass

    def buscar(self, codigo):
        # """
        # Devuelve el producto con el código indicado, o None si no existe.
        # """
        # buscar un producto por código
        pass

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        # """
        # Permite modificar los datos de un producto existente.
        # """
        # buscar el producto y actualizar sus atributos
        pass

    def eliminar(self, codigo):
        # """
        # Elimina un producto del inventario según su código.
        # """
        # eliminar el producto de la lista
        pass

    def valor_total(self):
        # """
        # Calcula y devuelve el valor total del inventario (precio * stock).
        # """
        # devolver la suma total del valor del stock
        pass

    def mostrar_por_proveedor(self, nombre_proveedor):
        # """
        # Muestra todos los productos de un proveedor determinado.
        # Si no existen productos de ese proveedor, mostrar un mensaje.
        # """
        # filtrar y mostrar los productos de un proveedor concreto
        pass


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

    # implementar las acciones correspondientes a cada opción del menú


if __name__ == "__main__":
    main()
