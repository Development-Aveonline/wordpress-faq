# Buzón de mejoras al harness

**El núcleo no se edita donde se lee.** Vive entre marcas en `CLAUDE.md` y `AGENTS.md`, se regenera
desde una fuente única, y un gate de la CI pone en rojo cualquier cambio hecho ahí. Eso es lo que
impide que existan cuarenta versiones distintas de la misma regla.

Pero una regla equivocada tiene que poder corregirse, y **quien la detecta casi nunca es quien
mantiene el harness**. Este es el camino.

## Cómo se propone algo

Creá un archivo acá, en **el repo donde apareció la necesidad**:

```
.harness/mejoras/mejora_harness_AAAAMMDD.md
```

Si ya hay uno con esa fecha: `mejora_harness_20260820_2.md`.

No pidas permiso ni abras una discusión antes. **Escribirlo en el momento es la mitad del valor**:
una mejora que se posterga "para cuando haya tiempo" se pierde, y la siguiente persona se choca con
lo mismo sin saber que ya le pasó a alguien.

Copiá `_plantilla.md` y llenalo.

## Qué pasa después

**Los revisan Juan o Alejandro** —cualquiera de los dos—, deciden y actualizan la fuente (`.ai/nucleo/NUCLEO.md` en
`app-v2`). Proponer no es aplicar: que este archivo exista no cambia ninguna regla hasta que se
acepta y se regenera.

Si se acepta, el archivo se marca como aplicado con la versión del núcleo que lo incorporó. Si se
rechaza, **también se responde acá, y con el motivo** — un buzón donde las cosas entran y nunca
sale nada deja de usarse a la tercera vez.
