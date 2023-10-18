#!/usr/bin/env python3
import itertools
import string
import gnupg
import time
import threading
import codecs
import re

characters = string.ascii_lowercase
length = 3
contrasennaEncontrada = False;
archivo_pass = "rockyouLowercase.txt"
lineas_procesadas = []
contrasenna = ""
lock = threading.Lock()


def contiene_palabras_con_numeros(linea):
    palabras = linea.split()
    for palabra in palabras:
        if re.search(r'\d', palabra):
            return True
    return False


with open(archivo_pass, "rb") as archivo:
    # Leer cada línea del archivo
    for linea in archivo:
        l_aux = linea.decode(errors="ignore")
        l_aux = l_aux.lower().strip()
        if str(l_aux).isascii() and not contiene_palabras_con_numeros(l_aux) and re.match(r'^[a-z]+$', l_aux):
            if len(l_aux) == 5:
                lineas_procesadas.append(l_aux)

with open("rockyou5.txt", "w") as archivo:
    for elemento in lineas_procesadas:
        archivo.write(elemento+"\n")
