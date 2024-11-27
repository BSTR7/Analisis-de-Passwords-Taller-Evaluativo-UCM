# Función para verificar si una letra es una vocal
def es_vocal(letra):
    return letra in "aeiou"  # Devuelve True si la letra es una de las vocales definidas

# Función para verificar si una letra es una consonante
def es_consonante(letra):
    return letra in "bcdfghjklmnpqrstvwxyz"  # Devuelve True si la letra está en la lista de consonantes

# Función principal para verificar si un password es "aceptable"
def es_aceptable(password):
    # Verificamos si tiene al menos una vocal
    tiene_vocal = any(es_vocal(letra) for letra in password)
    if not tiene_vocal:  # Si no tiene vocal, no es aceptable
        return False

    # Verificamos que no haya tres vocales o tres consonantes consecutivas
    for i in range(len(password) - 2):  # Iteramos sobre el password con un rango de 3 letras
        if (
            es_vocal(password[i]) and es_vocal(password[i+1]) and es_vocal(password[i+2]) or
            es_consonante(password[i]) and es_consonante(password[i+1]) and es_consonante(password[i+2])
        ):
            return False  # Si encuentra tres vocales o consonantes seguidas, no es aceptable

    # Verificamos que no haya letras repetidas consecutivamente (excepto "ee" y "oo")
    for i in range(len(password) - 1):  # Iteramos sobre pares consecutivos
        if password[i] == password[i+1] and password[i:i+2] not in ["ee", "oo"]:
            return False  # Si hay dos letras iguales seguidas (no permitidas), no es aceptable

    return True  # Si pasa todas las reglas, el password es aceptable

# Función para procesar las contraseñas desde un archivo de entrada y generar uno de salida
def procesar_claves(archivo_entrada, archivo_salida):
    # Abrimos el archivo de entrada (modo lectura) y el de salida (modo escritura)
    with open(archivo_entrada, "r") as entrada, open(archivo_salida, "w") as salida:
        for linea in entrada:  # Leemos cada línea del archivo de entrada
            password = linea.strip()  # Quitamos espacios en blanco o saltos de línea
            # Evaluamos si el password es aceptable o no
            if es_aceptable(password):
                salida.write(f"{password} -> Es aceptable.\n")  # Escribimos el resultado en el archivo de salida
            else:
                salida.write(f"{password} -> No es aceptable.\n")  # Escribimos el resultado en el archivo de salida

# Archivos de entrada y salida
entrada = "claves.txt"  # Nombre del archivo con los passwords a revisar
salida = "revisadas.txt"  # Nombre del archivo donde guardaremos los resultados

# Llamamos a la función para procesar los archivos
procesar_claves(entrada, salida)
