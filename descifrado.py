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
        """Decodificar la linea"""
        l_aux = linea.decode(errors="ignore")
        l_aux = l_aux.lower().strip()
        if str(l_aux).isascii() and not contiene_palabras_con_numeros(l_aux) and re.match(r'^[a-z]+$', l_aux):
            lineas_procesadas.append(l_aux)

def divideLista(lista:list, tamanno:int):
    tamannoSublista = len(lista) // (tamanno-1)
    sublistas = [lista[i:i + tamannoSublista] for i in range(0, len(lista), tamannoSublista)]
    return sublistas
    
def ProbarContraseña(id:int, combinations:list, f):
    i = 0
    gpg = gnupg.GPG()
    for password in combinations:
        i=i+1
        resultado = gpg.decrypt_file("archivo_cifrado.gpg", passphrase=password)
        
        if resultado.ok:
            print(f"Contraseña válida, iteración{i} desde el hilo:{id}")
            global contrasennaEncontrada, contrasenna
            contrasennaEncontrada = True
            lock.acquire()
            contrasenna = password
            lock.release()
            break
        if contrasennaEncontrada: break
        print(f"contraseña invalida iteración: {i} desde el hilo{id} pass probada:{password}")
        


hilos = []
#combinations = [''.join(combination) for combination in itertools.product(characters, repeat=3)]
listas_hilos = divideLista(lineas_procesadas, 10)
print(len(listas_hilos))
listas_hilos[1].insert(50, "qwerty")

descriptores = []
gpgs = []

for i in range(0,9):
    print(i)
    archivo = open("archivo_cifrado.gpg", "rb")

    descriptores.append(archivo)

for i in range(0, 9):
    hilo = threading.Thread(target=ProbarContraseña, args=(i, listas_hilos[i], descriptores[i],))
    hilos.append(hilo)
    hilo.start()
t1 = time.time()
for hilo in hilos:
    hilo.join();
t2 = time.time()
print(f'Contraseña encontrada :{contrasenna} Tiempo utilizado:{t2-t1}')