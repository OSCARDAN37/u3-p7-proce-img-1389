# =====================================================
# EJEMPLO 2: SOBEL X EN EL DOMINIO DE LA FRECUENCIA
# Oscar Flores Nc = 1389
# =====================================================
import numpy as np
import matplotlib.pyplot as plt
from funciones_frecuencia_1389 import (
    cargar_imagen,
    obtener_espectro,
    aplicar_filtro_frecuencia,
    normalizar_visualizacion,
    guardar_grafica
)

imagen = cargar_imagen()

sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=np.float32)

resultado_x = aplicar_filtro_frecuencia(imagen, sobel_x)
espectro_x = obtener_espectro(resultado_x)
imagen_x_normalizada = normalizar_visualizacion(resultado_x)

figura, ejes = plt.subplots(1, 3, figsize=(15, 5))

ejes[0].imshow(imagen, cmap="gray")
ejes[0].set_title("Imagen Original - 1389")
ejes[0].axis("off")

ejes[1].imshow(espectro_x, cmap="gray")
ejes[1].set_title("Espectro después de Sobel X - 1389")
ejes[1].axis("off")

ejes[2].imshow(imagen_x_normalizada, cmap="gray")
ejes[2].set_title("Respuesta Sobel X (Bordes Verticales) - 1389")
ejes[2].axis("off")

plt.tight_layout()
guardar_grafica(figura, "02_sobel_x.png")
plt.show()
print("Programa realizado pór Oscar Flores NC = 1389")