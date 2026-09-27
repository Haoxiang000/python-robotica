# Actividad 6 — Autonomía: las cuentas del robot

- *Módulo*: 2 · Variables y tipos
- *Fecha límite de entrega*: pendiente de apertura
- *RA 1*: d) Se han identificado los distintos tipos de variables. f) Se han creado y utilizado constantes y literales. h) Se han comprobado las conversiones de tipo.

## Contexto

Un sensor puede enviar la distancia como texto, por ejemplo `"45"`. Para trabajar con ella como número hay que convertirla. Además, las constantes permiten nombrar los datos fijos del robot.

## Objetivo

Combinar constantes, variables de distintos tipos y una conversión explícita, sin hacer cálculos.

## Lo que debes hacer

1. Crea `solucion/sensor.py`.
2. Declara estas constantes en MAYÚSCULAS:
   - `NOMBRE_SENSOR = "distancia"`.
   - `UNIDAD = "cm"`.
3. Declara `distancia_texto = "45"` y `bateria = 80`. Muestra el valor y el tipo de cada una.
4. Convierte explícitamente `distancia_texto` con `float()` y guarda el resultado en `distancia`. Muestra también el valor y el tipo de `distancia`.
5. Muestra todos los valores y tipos y guarda la salida en `solucion/sensor-salida.txt`.

## Entregable

- `solucion/sensor.py`.
- `solucion/sensor-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Las dos constantes están declaradas en MAYÚSCULAS | 25 % |
| Las variables tienen el tipo correcto | 25 % |
| La conversión con `float()` es explícita y se muestra su resultado | 30 % |
| La salida está guardada en `sensor-salida.txt` | 20 % |

## Pista de cara al futuro

Una constante puede contener texto o un número. Lo que la identifica como constante es su nombre en MAYÚSCULAS, no su tipo.
