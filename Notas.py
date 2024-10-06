# Módulo os para manejar operaciones del sistema de archivos
import os

# Nombre del archivo
nombre_archivo = "my_notes.txt"

# Crear y escribir en el archivo
with open(nombre_archivo, "w") as archivo:
    # Escribir tres notas
    archivo.write("1. nombre: Robinson Reyes. \n")
    archivo.write("2. edad: 43 años. \n")
    archivo.write("3. estatura: 1.65cm. \n")

print(f"Archivo '{nombre_archivo}' creado y escrito exitosamente.")

# Abrir y leer el archivo
print(f"\nContenido del archivo '{nombre_archivo}':")
with open(nombre_archivo, "r") as archivo:
    # Se lee el archivo línea por línea
    linea = archivo.readline()
    while linea:
        # Se muestra cada línea en la consola
        print(linea.strip())  # strip() para eliminar el salto de línea al final
        linea = archivo.readline()

# Verificar si el archivo existe y mostrar su tamaño
if os.path.exists(nombre_archivo):
    tamaño = os.path.getsize(nombre_archivo)
    print(f"\nEl archivo '{nombre_archivo}' existe y tiene un tamaño de {tamaño} bytes.")
else:
    print(f"\nEl archivo '{nombre_archivo}' no existe.")