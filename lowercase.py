#!/usr/bin/env python3
import re
archivo_entrada = "rockyou.txt"
archivo_salida = "rockyouLowercase.txt"

# Lista para almacenar las líneas procesadas
lineas_procesadas = []
def contiene_palabras_con_numeros(linea):
    palabras = linea.split()
    for palabra in palabras:
        if re.search(r'\d', palabra):
            return True
    return False

# Abrir el archivo de entrada en modo lectura
with open(archivo_entrada, "rb") as archivo:
    # Leer cada línea del archivo
    for linea in archivo:
        """Decodificar la linea"""
        l_aux = linea.decode(errors="ignore")
        l_aux = l_aux.lower().strip()
        if str(l_aux).isascii() and not contiene_palabras_con_numeros(l_aux) and re.match(r'^[a-z]+$', l_aux):
            lineas_procesadas.append(l_aux)

# Abrir el archivo de salida en modo escritura
with open(archivo_salida, "w") as archivo:
    # Escribir las líneas procesadas en el archivo de salida
    for linea in lineas_procesadas:
            if not contiene_palabras_con_numeros(linea):
                archivo.write(linea+"\r\n")

            

print(f"Se han procesado {len(lineas_procesadas)} líneas y se han guardado en {archivo_salida}.")
