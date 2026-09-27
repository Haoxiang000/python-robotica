# Actividad 5 — Convertir: el error de las comillas

- *Módulo*: 2 · Variables y tipos
- *Fecha límite de entrega*: pendiente de apertura
- *RA 1*: h) Se ha comprobado el funcionamiento de las conversiones de tipo explícitas e implícitas.

## Contexto

Cuando un sensor envía un número, puede llegar como texto: `"45"` no es lo mismo que `45`. Python conserva el tipo del valor, así que hay que convertirlo de forma explícita cuando necesitemos un número.

## Objetivo

Distinguir un valor de texto de un valor numérico y convertirlos con `int()`, `float()` y `str()`.

## Lo que debes hacer

1. Crea `solucion/conversiones.py`.
2. Declara `texto_entero = "3"` y muéstralo con su tipo usando `type()`.
3. Declara también `texto_decimal = "3.5"` y `numero = 42`. Convierte los valores explícitamente:
   - `texto_entero` con `int()`;
   - `texto_decimal` con `float()`;
   - `numero` con `str()`.
4. Muestra el valor y el tipo de cada valor convertido.
5. Ejecuta el programa y guarda la salida en `solucion/conversiones-salida.txt`.

## Entregable

- `solucion/conversiones.py`.
- `solucion/conversiones-salida.txt` con la salida de la consola.

## Criterios de evaluación

| Criterio | Peso |
|---|---|
| Se distingue el texto del número con `type()` | 25 % |
| `int()` convierte correctamente el texto entero | 25 % |
| `float()` y `str()` convierten correctamente los valores | 30 % |
| La salida está guardada en `conversiones-salida.txt` | 20 % |

## Pista de cara al futuro

`type()` te dice qué tipo tiene un valor. Usa esa misma función después de cada conversión para comprobar que el resultado es el que esperabas.
