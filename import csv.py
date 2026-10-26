import csv
import os

def filtrar_mayores_de_edad():
    try:
        # Paso 1: Abrir y leer el archivo CSV usando la librería csv
        with open('todas_las_personas.csv', mode='r', encoding='utf-8') as archivo_csv:
            lector = csv.reader(archivo_csv)
            
            # Paso 3: Crear/abrir el nuevo archivo de texto plano para escritura
            with open('mayores_de_edad.txt', mode='w', encoding='utf-8') as archivo_txt:
                
                # Paso 2: Procesar fila por fila
                for fila in lector:
                    if len(fila) >= 2:
                        nombre = fila[0].strip()
                        # Extraer la edad y convertirla a número entero
                        edad = int(fila[1].strip())
                        
                        # Verificar si la persona tiene 18 años o más
                        if edad >= 18:
                            # Guardar el nombre en el archivo de texto
                            archivo_txt.write(nombre + '\n')
                            
        print("El filtrado se ha completado con éxito. Revisa el archivo 'mayores_de_edad.txt'.")

    except FileNotFoundError:
        # Paso 4: Protección en caso de que el archivo CSV no exista
        print("Error: El archivo 'todas_las_personas.csv' no se encuentra en el directorio.")




filtrar_mayores_de_edad()