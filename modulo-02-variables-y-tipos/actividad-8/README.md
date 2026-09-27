# Actividad 8 — Depura tu propio código

- *Módulo*: 2 · Variables y tipos
- *Fecha límite de entrega*: pendiente de apertura
- *RA 3*: f) Se han probado y depurado los programas. g) Se ha comentado y documentado el código.

## Contexto

Nadie escribe código bien a la primera. Cuando un programa falla, el mensaje de error es una pista: indica qué esperaba Python y qué encontró.

## Objetivo

Practicar la búsqueda y corrección de errores simples leyendo el mensaje que muestra Python.

## Lo que debes hacer

1. Crea `solucion/depuracion.py` con un programa que deba mostrar el nombre del robot, una distancia recibida como texto y si el robot está encendido.
2. Introduce un error y ejecuta el programa. Copia el mensaje real en `solucion/errores.txt`, corrige el error y repite el proceso con otros dos errores, uno cada vez.
3. Después de cada corrección, vuelve a ejecutar el programa y usa `print()` para comprobar que funciona. No hace falta usar el depurador del editor.
4. Documenta cada fallo en un `README.md` dentro de `solucion/` con tres líneas: **qué esperaba**, **qué pasó** y **por qué**.
5. Deja el programa final funcionando, con al menos tres comentarios que expliquen las correcciones, y guarda su salida en `solucion/depuracion-salida.txt`.

## Entregable

- `solucion/depuracion.py` funcionando.
- `solucion/errores.txt` con los tres mensajes originales.
- `solucion/README.md` con la documentación de los tres fallos.
- `solucion/depuracion-salida.txt` con la salida final.
- Al menos tres commits: uno por cada error corregido.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| El programa final muestra los datos esperados | 30 % |
| Los tres fallos están documentados con el mensaje real | 30 % |
| Cada corrección se comprueba ejecutando y usando `print()` | 20 % |
| El proceso se ve en los commits y en la documentación | 20 % |

## Pista de cara al futuro

Cuando el robot tenga sensores, los errores serán la norma y no la excepción. Leer el mensaje, cambiar una cosa y volver a probar es el ciclo de depuración.
