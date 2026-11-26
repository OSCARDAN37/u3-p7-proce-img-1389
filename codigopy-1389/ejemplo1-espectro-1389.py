# =====================================================
# EJEMPLO 1: IMAGEN ORIGINAL Y ESPECTRO DE FRECUENCIA
# Oscar Flores Nc = 1389
# =====================================================
import matplotlib.pyplot as plt
from funciones_frecuencia_1389 import (
    cargar_imagen,
    obtener_espectro,
    guardar_grafica
)

imagen = cargar_imagen()
espectro = obtener_espectro(imagen)

print("--- EJEMPLO 1 ---")
print("Imagen papa1.jpg cargada.")
print(f"Dimensiones: Alto={imagen.shape[0]}, Ancho={imagen.shape[1]}")

figura, ejes = plt.subplots(1, 2, figsize=(12, 6))

ejes[0].imshow(imagen, cmap="gray")
ejes[0].set_title("Imagen Original (Dominio Espacial) - 1389")
ejes[0].axis("off")

ejes[1].imshow(espectro, cmap="gray")
ejes[1].set_title("Espectro de Frecuencia (Dominio de Frecuencia) - 1389")
ejes[1].axis("off")

plt.tight_layout()

guardar_grafica(figura, "01_imagen_y_espectro.png")
plt.show()
print("Programa realizado pór Oscar Flores NC = 1389")