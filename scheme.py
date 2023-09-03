import random
import time
import cv2

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

# Transmisor -> FALTA CONVERTIR A BINARIO
class Transmisor:
    def __init__(self, fuente, canal):
        self.fuente = fuente
        self.canal = canal

    def transmitir(self):
        while True:
            frame = self.fuente.generar_datos()
            if frame is None:
                break
            #paquete = PaqueteVideo(frame)
            self.canal.enviar(frame)
            
# Canal de Comunicación
class CanalComunicacion:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def enviar(self, paquete):
        # Simula el canal de comunicación con una probabilidad de pérdida de paquetes
        if random.random() < 0.5:  # Probabilidad de pérdida del 30%
            print("Paquete perdido:", paquete)
        else:
            # Simula la velocidad de 802.11n
            time.sleep(self.velocidad)
            self.retransmitir(paquete)

    def retransmitir(self, paquete):
        #print("Paquete enviado:", paquete)
        # Simula la retransmisión del paquete al receptor
        receptor.recibir(paquete)

# Receptor
class Receptor:
    def __init__(self, fps, ancho, altura):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_salida = cv2.VideoWriter('one_piece_recibido.mp4', fourcc, fps, (ancho, altura))

    def recibir(self, paquete):
        frame = paquete
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
    canal = CanalComunicacion(0.01)  # Velocidad de 802.11n simulada (0.1 segundos) (MODIFICAR)
    receptor = Receptor(fuente.fps, fuente.ancho, fuente.altura)
    transmisor = Transmisor(fuente, canal)

    transmisor.transmitir()
    receptor.cerrar_video()