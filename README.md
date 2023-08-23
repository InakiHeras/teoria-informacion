# teoria-informacion

Como fuente de información utilizaré la API de IMDb de RapidAPI que proporciona datos sobre películas en un json. Como método de transmisión planeo invertir la información (transformada en binario), cuando llegue al receptor este debera revertirla (como usar [::-1] en un string). No pienso usar un protocolo, pero si paquetes. Planeo usar la libreria "threading" de python ya que con el manejo de hilos puedo ejecutar funciones en paralelo y monitorear las entradas y salidas en tiempo real, lo que serviria como el canal. Dentro de la función de método de transmisión planeo simular la velocidad de la fibra óptica (una velocidad simulada de 100 Gbps) con un sleep para simular la velocidad de transmisión. 
