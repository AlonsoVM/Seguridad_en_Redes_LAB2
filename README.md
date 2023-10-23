# Seguridad_en_Redes_LAB2

## Preparar el entorno para la ejecución:
 * Primero crearemos un entorno virtual con python para instalar las dependencias del proyecto, para ello ejecutamos el siguiente comando:
    *   **python -m venv nombre_del_entorno**

 * Activamos el entorno virtual:
    *   **source nombre_del_entorno/bin/activate**

 * Luego instalaremos las dependencias del proyecto, estas se encuentra en el archivo **requirements.txxt**
    *   **pip install -r requirements.txt**

## Como ejecutar el proyecto:
 * Para indicar el archivo que deseamos descifrar usamos la opción **-f**
 * Para indicar el numero de hilos a utilizar utilizamos la opción **-t**
 * Para indicar el archivo de salida utilizamos la opción **-o**

## Ejemplo de una ejecución:
 * **./bruteForce.py -f archivo.pdf.gpg -t 12 -o archivo.pdf**

## Consideraciones:
Cabe destecar que la opción **por defecto** que esta activada para el **número de hilos es de 10**, ya que es con la que se ha obtenido un mejor rendimiento probando las combinaciones de 2 carácteres, realizando entre 12 y 13 combinaciones por segundo.
Por defecto **no se selecciona ningún archivo como entrada**, por lo que si no se indica un archivo el programa **fallará**, en el caso del archivo de salida, será **solution**.

## Solución:
La solución que hemos encontrado es que la contraseña es **sgrd**, para ello la aplicación ha ido probando primero con las convinaciones de 1, 2 y 3 carácteres, hasta llegar a las de 4 donde termina al probar la contraseña. El archivo desencriptado de encuentra en **archivo.pdf**