Proyecto de la practica de Sistemas Expertos. Implementa un motor de
inferencia con encadenamiento hacia adelante (forward chaining) usando la
libreria [`experta`](https://github.com/nilp0inter/experta), para hacer
diagnosticos medicos simples a partir de combinaciones de sintomas.

## Estructura del proyecto

- `sistema_experto.py`: define los hechos (`Sintoma`, `Diagnostico`) y la
  clase `SistemaDiagnostico`, que hereda de `KnowledgeEngine` y contiene
  todas las reglas de diagnostico.
- `main.py`: ejecuta los cinco casos de prueba de la Parte 3, mas los casos
  de las nuevas enfermedades del Ejercicio 1 y el caso de conflicto de
  reglas del Ejercicio 2, mostrando la salida de cada uno.
- `reflexion.md`: respuestas a las preguntas de reflexion.

## Reglas implementadas

| Enfermedad | Sintomas requeridos |
|---|---|
| Gripe | fiebre, tos, dolor de garganta |
| Migrana | fiebre, dolor de cabeza, nauseas |
| Alergia | estornudos, congestion nasal, picazon en los ojos |
| Gastroenteritis | dolor de estomago, diarrea, vomitos |
| COVID-19 | fiebre, tos seca, perdida de olfato |
| Resfriado comun | congestion nasal, estornudos, tos leve |
| Bronquitis | tos persistente, flema, dificultad respiratoria |
| Dengue | dolor articular, sarpullido, fiebre |

Ademas existe una regla de respaldo (`sin_diagnostico`) que se activa solo
cuando ninguna de las reglas anteriores genero un `Diagnostico`, usando la
condicion `NOT(Diagnostico())`.

## Requisitos

- Python 3.x
- Libreria `experta`:

```bash
pip install experta
```

> Nota: `experta` depende de `frozendict` y `schema`; en instalaciones
> recientes de Python puede ser necesario instalar una version compatible
> (por ejemplo `pip install experta frozendict==2.3.4` si aparece un error
> de compatibilidad).

## Como ejecutar

```bash
python main.py
```

Esto imprime en pantalla, para cada caso de prueba, el diagnostico obtenido
y su recomendacion asociada.

## Casos de prueba incluidos

1. Fiebre, tos y dolor de garganta -> Gripe.
2. Estornudos, congestion nasal y picazon en los ojos -> Alergia.
3. Dolor de estomago, diarrea y vomitos -> Gastroenteritis.
4. Cansancio y mareo (no coincide con ninguna regla) -> se activa la regla
   de respaldo.
5. Fiebre, tos, dolor de garganta, estornudos y congestion nasal -> se
   cumplen las condiciones de Gripe (Alergia no se activa porque falta el
   sintoma de picazon en los ojos).
6. Fiebre, tos seca y perdida de olfato -> COVID-19.
7. Congestion nasal, estornudos y tos leve -> Resfriado comun.
8. Tos persistente, flema y dificultad respiratoria -> Bronquitis.
9. Dolor articular, sarpullido y fiebre -> Dengue.
10. Sintomas de Gripe y Alergia a la vez -> se activan ambas reglas (ver
    `reflexion.md` para el analisis del Ejercicio 2).
