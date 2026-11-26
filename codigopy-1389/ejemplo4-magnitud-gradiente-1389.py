# =====================================================
# EJEMPLO 4: MAGNITUD DEL GRADIENTE (SOBEL X + SOBEL Y)
# Oscar Flores NC = 1389
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

sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)

resultado_x = aplicar_filtro_frecuencia(imagen, sobel_x)
resultado_y = aplicar_filtro_frecuencia(imagen, sobel_y)

magnitud_gradiente = np.sqrt(resultado_x**2 + resultado_y**2)

img_x_norm = normalizar_visualizacion(resultado_x)
img_y_norm = normalizar_visualizacion(resultado_y)
img_mag_norm = normalizar_visualizacion(magnitud_gradiente)

espectro_x = obtener_espectro(resultado_x)
espectro_y = obtener_espectro(resultado_y)

figura, ejes = plt.subplots(2, 3, figsize=(18, 10))

ejes[0, 0].imshow(imagen, cmap="gray")
ejes[0, 0].set_title("1. Imagen Original - 1389")
ejes[0, 0].axis("off")

ejes[0, 1].imshow(espectro_x, cmap="gray")
ejes[0, 1].set_title("2. Espectro Sobel X - 1389")
ejes[0, 1].axis("off")

ejes[0, 2].imshow(espectro_y, cmap="gray")
ejes[0, 2].set_title("3. Espectro Sobel Y - 1389")
ejes[0, 2].axis("off")

ejes[1, 0].imshow(img_x_norm, cmap="gray")
ejes[1, 0].set_title("4. Respuesta Sobel X (Verticales) - 1389")
ejes[1, 0].axis("off")

ejes[1, 1].imshow(img_y_norm, cmap="gray")
ejes[1, 1].set_title("5. Respuesta Sobel Y (Horizontales) - 1389")
ejes[1, 1].axis("off")

ejes[1, 2].imshow(img_mag_norm, cmap="gray")
ejes[1, 2].set_title("6. Magnitud del Gradiente (Todos los bordes) - 1389")
ejes[1, 2].axis("off")

plt.tight_layout()
guardar_grafica(figura, "04_comparacion_magnitud_gradiente.png")
plt.show()
print("Programa realizado pór Oscar Flores NC = 1389")