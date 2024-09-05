class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        """Inserta un elemento en el heap."""
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """Elimina y devuelve el elemento mínimo."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Intercambia la raíz con el último elemento y reduce el tamaño del heap.
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        """Mantiene la propiedad del heap al insertar un nuevo elemento."""
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            # Intercambia el nodo con su padre si es menor.
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Recursivamente ajusta el heap hacia arriba.
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """Mantiene la propiedad del heap al extraer el elemento mínimo."""
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        # Compara el nodo con sus hijos y encuentra el menor.
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        # Si el nodo no es el menor, intercámbialo con el menor hijo y sigue ajustando.
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        """Devuelve el elemento mínimo sin extraerlo."""
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def size(self):
        """Devuelve el tamaño del heap."""
        return len(self.heap)

    def is_empty(self):
        """Devuelve si el heap está vacío."""
        return len(self.heap) == 0