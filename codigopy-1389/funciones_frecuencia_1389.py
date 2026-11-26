# =====================================================
# ARCHIVO: funciones_frecuencia_1389.py
# PROPÓSITO: Funciones compartidas para procesamiento en frecuencia
# Oscar Flores NC = 1389
# =====================================================
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

def cargar_imagen():
    imagen = cv2.imread("papa1.jpg", cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        raise FileNotFoundError("No se encontró 'papa1.jpg'. Verifica que esté en la carpeta principal u3-p7-proce-img-img-1389.")
    return imagen

def obtener_espectro(imagen):
    f_transform = np.fft.fft2(imagen)
    f_shift = np.fft.fftshift(f_transform)
    espectro = 20 * np.log(np.abs(f_shift) + 1)
    return espectro

def aplicar_filtro_frecuencia(imagen, kernel):
    pad_size = 1
    imagen_padded = np.pad(imagen, pad_size, mode='reflect')
    rows, cols = imagen_padded.shape
    
    kernel_padded = np.zeros((rows, cols), dtype=np.float32)
    k_rows, k_cols = kernel.shape
    start_r = (rows - k_rows) // 2
    start_c = (cols - k_cols) // 2
    kernel_padded[start_r:start_r+k_rows, start_c:start_c+k_cols] = kernel
    
    kernel_padded_shifted = np.fft.ifftshift(kernel_padded)
    
    fft_img = np.fft.fft2(imagen_padded)
    fft_ker = np.fft.fft2(kernel_padded_shifted)
    
    resultado_fft = fft_img * fft_ker
    
    resultado_complejo = np.fft.ifft2(resultado_fft)
    resultado_real = np.real(resultado_complejo)
    
    return resultado_real[pad_size:-pad_size, pad_size:-pad_size]

def normalizar_visualizacion(imagen):
    imagen_abs = np.abs(imagen)
    imagen_normalizada = cv2.normalize(
        imagen_abs, None, 0, 255, cv2.NORM_MINMAX
    )
    return imagen_normalizada.astype(np.uint8)

def guardar_grafica(figura, nombre_archivo):
    carpeta = "resultados-img-1389"
    os.makedirs(carpeta, exist_ok=True)
    ruta = os.path.join(carpeta, nombre_archivo)
    figura.savefig(ruta, dpi=150, bbox_inches="tight")
    print(f"Imagen guardada correctamente en: {ruta}")
print("Programa realizado pór Oscar Flores NC = 1389")