import random
import time
import cv2
import struct
import numpy as np
import math

# Fuente de Información -> VIDEO
class FuenteInformacion:
    def __init__(self, video):
        self.video = cv2.VideoCapture(video)
        self.fps = int(self.video.get(cv2.CAP_PROP_FPS))
        self.ancho = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.altura = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def generar_datos(self):
        # Leer frame por frame
        ret, frame = self.video.read()
        if not ret:
            # Si llegamos al final del video, regresa un None
            return None
        return frame 

# Transmisor
class Transmisor:
    def __init__(self, fuente, canal):
        self.fuente = fuente
        self.canal = canal

    def transmitir(self):
        while True:
            frame = self.fuente.generar_datos()
            if frame is None:
                break
            paquete = struct.pack(f'{frame.size}s', frame.tobytes())
            self.canal.enviar(paquete)
            
# Canal de Comunicación
class CanalComunicacion:
    def __init__(self, velocidad):
        self.velocidad = velocidad
        self.ruido_list = []

    def enviar(self, paquete):
        # Simula el canal de comunicación con una probabilidad de pérdida de paquetes
        if random.random() < 0.3:  # Probabilidad de pérdida
            #print("Paquete corrupto")
            paquete_corrupto = self.introducir_ruido(paquete)
            self.retransmitir(paquete_corrupto)
            self.ruido_list.append(random.random())
        else:
            # Simula la velocidad de 802.11n
            time.sleep(self.velocidad)
            self.retransmitir(paquete)

    def retransmitir(self, paquete):
        #print("Paquete enviado:", paquete)
        # Simula la retransmisión del paquete al receptor
        receptor.recibir(paquete)

    def introducir_ruido(self, paquete):
        # Cambiar aleatoriamente algunos bytes del paquete
        paquete_corrupto = bytearray(paquete)
        num_errores = random.randint(1, int(0.4 * len(paquete))) # Simular hasta el 40% de errores
        for _ in range(num_errores):
            indice = random.randint(0, len(paquete_corrupto) - 1)
            paquete_corrupto[indice] = random.randint(0, 255) # Cambiar a un valor aleatorio de 0 a 255
        return bytes(paquete_corrupto)
    
    def calcular_entropia(self):
        probabilidades = [num / len(self.ruido_list) if num < 0.3 else 0 for num in self.ruido_list]
        entropia = -sum(p * math.log2(p) for p in probabilidades if p > 0)
        return entropia


# Receptor
class Receptor:
    def __init__(self, fps, ancho, altura):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_salida = cv2.VideoWriter('one_piece_recibido.mp4', fourcc, fps, (ancho, altura))

    def recibir(self, paquete):
        frame = np.frombuffer(struct.unpack(f'{len(paquete)}s', paquete)[0], dtype=np.uint8)
        frame = frame.reshape((fuente.altura, fuente.ancho, 3))
        self.video_salida.write(frame)
    
    def cerrar_video(self):
        self.video_salida.release()

'''
class PaqueteVideo:
    def __init__(self, frame):
        self.frame = frame
'''
# Función principal
if __name__ == "__main__":
    # Crear objetos de las clases
    fuente = FuenteInformacion('one_piece.mp4')
    canal = CanalComunicacion(0.01)  # Velocidad de 802.11n simulada (0.1 segundos)
    receptor = Receptor(fuente.fps, fuente.ancho, fuente.altura)
    transmisor = Transmisor(fuente, canal)

    transmisor.transmitir()
    receptor.cerrar_video()

    entropia = canal.calcular_entropia()
    print(entropia)