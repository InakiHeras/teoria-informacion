import random
import time
import queue
import threading

# Fuente de Información
class FuenteInformacion:
    def generar_datos(self):
        # Genera datos de la fuente de información (en este caso, números aleatorios) (MODIFICAR)
        return [random.randint(0, 255) for _ in range(10)]  # Ejemplo de 10 números entre 0 y 255

# Transmisor -> FALTA CONVERTIR A BINARIO
class Transmisor:
    def __init__(self, fuente, canal):
        self.fuente = fuente
        self.canal = canal

    def transmitir(self):
        datos = self.fuente.generar_datos()
        for dato in datos:
            paquete = PaqueteUDP(dato)
            self.canal.enviar(paquete)

# Canal de Comunicación
class CanalComunicacion:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def enviar(self, paquete):
        # Simula el canal de comunicación con una probabilidad de pérdida de paquetes
        if random.random() < 0.3:  # Probabilidad de pérdida del 30%
            print("Paquete perdido:", paquete)
        else:
            # Simula la velocidad de 802.11n
            time.sleep(self.velocidad)
            self.retransmitir(paquete)

    def retransmitir(self, paquete):
        print("Paquete enviado:", paquete)
        # Simula la retransmisión del paquete al receptor
        receptor.recibir(paquete)

# Receptor
class Receptor:
    def recibir(self, paquete):
        # Simula la recepción del paquete por el receptor
        print("Paquete recibido por el receptor:", paquete)

# Clase que representa un paquete UDP con encabezado y cola
class PaqueteUDP:
    def __init__(self, dato):
        self.encabezado = "UDP_HEADER"
        self.dato = dato
        self.cola = "UDP_TAIL"

    def __str__(self):
        return f"{self.encabezado} {self.dato} {self.cola}"

# Función principal
if __name__ == "__main__":
    # Crear objetos de las clases
    fuente = FuenteInformacion()
    canal = CanalComunicacion(0.1)  # Velocidad de 802.11n simulada (0.1 segundos) (MODIFICAR)
    receptor = Receptor()

    # Crear y ejecutar hilos para el transmisor
    transmisor = Transmisor(fuente, canal)
    transmisor_thread = threading.Thread(target=transmisor.transmitir)
    transmisor_thread.start()
    transmisor_thread.join()
