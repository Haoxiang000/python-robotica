# Actividad 2 — La ficha del robot

- *Módulo*: 2 · Variables y tipos
- *Fecha límite de entrega*: pendiente de apertura
- *RA 1*: d) Se han identificado los distintos tipos de variables y la utilidad específica de cada uno. e) Se ha modificado el código de un programa para crear y utilizar variables.

## Contexto

Todo lo que un robot sabe de sí mismo (su nombre, cuántas ruedas tiene, cuánto pesa la batería, si está encendido) acaba guardado en variables. Darle nombre a cada dato es el primer paso para trabajar con él.

## Objetivo

Crear variables de distintos tipos y comprobar su valor y su tipo.

## Lo que debes hacer

1. Crea `solucion/ficha.py` con las siguientes variables:
   - `nombre` (texto): el nombre de tu robot.
   - `ruedas` (entero): cuántas ruedas tiene.
   - `diametro_rueda` (decimal): el diámetro en centímetros.
   - `bateria` (entero): los minutos de autonomía que le quedan.
   - `encendido` (booleano): si está encendido o no.
2. Muestra cada variable en una sola línea con su nombre, su valor y su tipo. Usa `type()` para obtener el tipo. Por ejemplo, si `nombre = "Titán"`, la línea puede parecerse a `nombre: Titán (str)`.
3. Ejecuta el programa, comprueba que cada variable tiene el tipo esperado y guarda la salida en `solucion/ficha-salida.txt`.

## Entregable

- `solucion/ficha.py`.
- `solucion/ficha-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Las 5 variables existen con el tipo correcto | 40 % |
| Se muestra el nombre, el valor y el tipo de cada variable | 25 % |
| Nombres de variables claros y sin acentos ni espacios | 10 % |
| La salida está guardada en `ficha-salida.txt` | 25 % |

## Pista de cara al futuro

Estas variables describen el robot. Fíjate en cuál es texto, cuál es número y cuál es booleano: cada tipo sirve para una cosa distinta.
