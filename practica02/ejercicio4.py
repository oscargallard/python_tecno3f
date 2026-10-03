try:
    # Intentamos abrir el archivo en modo lectura ('r')
    archivo = open("mi_archivo.txt", "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()
except FileNotFoundError:
    print("El archivo no existe. Creando uno nuevo...")
    # Creamos el archivo abriéndolo en modo escritura ('w')
    nuevo_archivo = open("mi_archivo.txt", "w")
    nuevo_archivo.write("No todo lo que brilla es oro.")
    nuevo_archivo.close()
    print("Archivo creado con éxito.-")