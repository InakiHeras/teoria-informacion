import cv2
import numpy as np
import heapq

class Nodo:
    def __init__(self, sim, freq, left=None, right=None):
        self.freq = freq
        self.sim = sim
        self.left = left
        self.right = right
        self.huff = ''

    #  Determina qué elemento tiene la mayor prioridad y, por lo tanto, se extrae primero
    def __lt__(self, siguiente):
        return self.freq < siguiente.freq

def codigoHuffman(lista):
  freq = {}
  for elemento in lista:
    if elemento in freq:
      freq[elemento] += 1
    else:
      freq[elemento] = 1

  # Crear un nodo hoja para cada símbolo, asociando un peso según su frecuencia de aparición e insertarlo en la lista ordenada ascendentemente.
  nodos = [Nodo(simbolo, frecuencia) for simbolo, frecuencia in freq.items()]
  heapq.heapify(nodos)

  # Mientras haya mas de un nodo en la lista.
  while len(nodos) > 1:
    # Eliminar los dos nodos con menos probabilidad de la lista
    nodo_izquierdo = heapq.heappop(nodos)
    nodo_derecho = heapq.heappop(nodos)
    # Asignar valor direccional
    nodo_izquierdo.huff = 0
    nodo_derecho.huff = 1
    # Crear un nuevo nodo interno que enlace a los nodos anteriores, asignándoles como peso la suma de los pesos de los nodos hijos.
    nuevo_nodo = Nodo(None, nodo_izquierdo.freq + nodo_derecho.freq)
    nuevo_nodo.left = nodo_izquierdo
    nuevo_nodo.right = nodo_derecho
    heapq.heappush(nodos, nuevo_nodo)

  return nodos[0]

def imprimirNodos(nodo, val=''):
  nuevoVal = val + str(nodo.huff)

  if nodo.left:
    imprimirNodos(nodo.left, nuevoVal)
  if nodo.right:
    imprimirNodos(nodo.right, nuevoVal)

  if not nodo.left and not nodo.right:
    print(f"{nodo.sim} -> {nuevoVal}")

if __name__ == "__main__":
    image = cv2.imread('imagen.jpg')

    if image is None:
        print('No se pudo cargar la imagen')
    else:    
        imageToBinary = ''.join(format(byte, '08b') for byte in image.tobytes())
        # Divide la cadena binaria en paquetes de 8 bits y los almacena en una lista
        packet_list = [imageToBinary[i:i+8] for i in range(0, len(imageToBinary), 8)]

    arbol = codigoHuffman(packet_list)
    imprimirNodos(arbol)

