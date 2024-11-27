# **Análisis de Passwords - Taller Evaluativo**

---

## **Descripción del proyecto**
Este programa ha sido desarrollado como parte de un taller evaluativo de la **Universidad Católica del Maule**, enfocado en la carrera de **Ingeniería de Ejecución Geomensura**. Su propósito es validar un conjunto de contraseñas potenciales para determinar si cumplen con las reglas establecidas para ser consideradas **"aceptables"** según criterios de seguridad y facilidad de memorización.

El programa lee contraseñas desde un archivo de entrada (`claves.txt`), las analiza y genera un archivo de salida (`revisadas.txt`) con el resultado de cada validación.

---

## **Reglas de aceptación de passwords**
Un password es considerado **aceptable** si cumple con las siguientes condiciones:

1. Contiene al menos una vocal (`a, e, i, o, u`).
2. No tiene tres vocales consecutivas ni tres consonantes consecutivas.
3. No tiene dos ocurrencias consecutivas de la misma letra, **excepto** para los pares `"ee"` o `"oo"`.

> **Notas importantes:**
> - Las vocales están definidas como `a, e, i, o, u`.  
> - Las consonantes son todas las demás letras del alfabeto en minúscula (`b, c, d, f, g, h, ..., z`), excluyendo letras con tildes o la letra "ñ".  
> - El archivo de entrada sólo debe contener letras en minúsculas, una contraseña por línea.

---

## **Estructura de archivos**

### 1. **Archivo de entrada** (`claves.txt`)
Debe contener una lista de posibles contraseñas, con **una contraseña por línea**. Ejemplo de contenido:

a tv ptoui bontres zoggax wiinq eep houctuh hugo


### 2. **Archivo de salida** (`revisadas.txt`)
El programa genera este archivo indicando si cada contraseña es aceptable o no. Ejemplo de salida:

a -> Es aceptable. tv -> No es aceptable. ptoui -> No es aceptable. bontres -> No es aceptable. zoggax -> No es aceptable. wiinq -> No es aceptable. eep -> Es aceptable. houctuh -> Es aceptable. hugo -> Es aceptable.

---

## **Requisitos**

- Python 3.x instalado en tu sistema.
- Conocimientos básicos en programación y manejo de archivos.
- Archivo de entrada (`claves.txt`) en el mismo directorio que el programa.

---
