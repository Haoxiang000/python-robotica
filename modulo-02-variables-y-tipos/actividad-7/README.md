# Actividad 7 — El perfil completo del robot

- *Módulo*: 2 · Variables y tipos
- *Fecha límite de entrega*: pendiente de apertura
- *RA 1*: d), e), f) y h) de los tipos de variables, constantes, literales y conversiones.

## Contexto

Con variables, constantes y conversiones ya se puede describir un robot entero. Esta actividad combina lo aprendido hasta ahora, sin introducir condiciones ni fórmulas.

## Objetivo

Combinar los cuatro tipos de datos y una constante en una ficha sencilla.

## Lo que debes hacer

1. Crea `solucion/perfil.py`.
2. Declara al menos estas variables, cada una con su tipo:
   - `nombre` (str).
   - `anio` (int).
   - `altura_cm` (float).
   - `autonomo` (bool).
3. Declara la constante `VERSION_ESPERADA = "v1.0"` en MAYÚSCULAS.
4. Imprime una línea por variable con su nombre, su valor y su tipo. Usa `print()` y `type()`; no hace falta alinear las líneas.
5. Ejecuta el programa y guarda la salida en `solucion/perfil-salida.txt`.

## Entregable

- `solucion/perfil.py`.
- `solucion/perfil-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Están presentes los cuatro tipos de datos | 40 % |
| La constante está declarada en MAYÚSCULAS y se muestra | 20 % |
| Se muestra el nombre, el valor y el tipo de cada variable | 20 % |
| La salida está guardada en `perfil-salida.txt` | 20 % |

## Pista de cara al futuro

El valor y el tipo son cosas distintas: `80` es un valor entero y `int` es su tipo. Mostrar los dos te ayuda a comprobar que has declarado la variable como querías.
