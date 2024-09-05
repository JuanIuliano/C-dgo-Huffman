class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
 
class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
 
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_rec(self.raiz, valor)
 
    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_rec(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_rec(nodo.derecha, valor)
 
    def buscar(self, valor):
        return self._buscar_rec(self.raiz, valor)
 
    def _buscar_rec(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_rec(nodo.izquierda, valor)
        else:
            return self._buscar_rec(nodo.derecha, valor)
 
    def imprimir_en_orden(self):
        self._imprimir_en_orden_rec(self.raiz)
 
    def _imprimir_en_orden_rec(self, nodo):
        if nodo:
            self._imprimir_en_orden_rec(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._imprimir_en_orden_rec(nodo.derecha)
 
# Ejemplo de uso:
arbol = ArbolBinarioBusqueda()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)
 
print("Impresión en orden del árbol:")
arbol.imprimir_en_orden()  # Salida esperada: 2 3 4 5 6 7 8