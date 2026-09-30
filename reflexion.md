# Respuestas de reflexion

## Ejercicio 2: Analisis de conflicto de reglas

Caso de prueba: se declaran a la vez los sintomas de Gripe (fiebre, tos,
dolor de garganta) y de Alergia (estornudos, congestion nasal, picazon en
los ojos).

- **Cuantos diagnosticos se generan:** dos. Se declaran los hechos
  `Diagnostico(enfermedad="Gripe")` y `Diagnostico(enfermedad="Alergia")`,
  porque ambos conjuntos de condiciones se cumplen simultaneamente en la
  memoria de trabajo y ninguna de las dos reglas excluye a la otra.
- **Orden de ejecucion:** ambas reglas quedan en la agenda del motor en el
  mismo ciclo, ya que sus condiciones se satisfacen desde el primer
  `engine.run()`. `experta`, al no definirse una `salience` explicita,
  resuelve el orden de disparo segun la estrategia de resolucion de
  conflictos por defecto (basada en el orden de activacion/especificidad de
  las reglas en la agenda), que en la practica tiende a coincidir con el
  orden en que las reglas quedaron definidas en la clase.
- **Dependencia del orden de definicion:** si, el resultado final (la lista
  de diagnosticos) no cambia, porque ambas reglas se activan
  independientemente y ninguna depende de que la otra se ejecute primero.
  Sin embargo, el orden en que se imprimen los mensajes en pantalla si
  puede depender del orden de definicion de las reglas dentro de la clase
  (o de la salience si se configurara), porque eso determina cual entra
  primero a la agenda de ejecucion.

## Preguntas de reflexion

**1. Que limitaciones observaste en este enfoque durante la practica**

El sistema solo reconoce combinaciones exactas de sintomas: si al paciente
le falta un solo sintoma de los requeridos (por ejemplo, tiene fiebre y tos
pero no dolor de garganta), ninguna regla se activa aunque clinicamente el
cuadro sea muy parecido a una gripe. Ademas, los sintomas son estrictamente
booleanos (presente o ausente), no admiten grados de intensidad ni
probabilidad, y el conocimiento medico real necesitaria muchas mas reglas,
excepciones y combinaciones para acercarse a un diagnostico confiable. El
sistema tampoco pondera la gravedad ni el contexto del paciente (edad,
historial, duracion de los sintomas), y al agregar mas reglas aumenta el
riesgo de que se solapen o contradigan entre si.

**2. Como podria manejarse la incertidumbre en los sintomas (por ejemplo, un
sintoma presente solo parcialmente)**

Una opcion es reemplazar los valores booleanos por factores de certeza o
probabilidades (por ejemplo, un valor entre 0 y 1 que indique que tan
presente esta el sintoma) y definir umbrales minimos para activar cada
regla, combinando los factores de certeza de los sintomas involucrados con
alguna formula (suma ponderada, minimo, o reglas de combinacion tipo
Dempster-Shafer). Otra alternativa es usar logica difusa (fuzzy logic),
donde cada sintoma tiene un grado de pertenencia a conjuntos como "leve",
"moderado" o "severo", y las reglas trabajan con esos grados en lugar de
valores estrictamente verdadero/falso. Tambien se podrian usar enfoques
probabilisticos (redes bayesianas) que permitan calcular la probabilidad de
cada diagnostico dado un conjunto de evidencias parciales, en vez de un
sistema de reglas rigido.

**3. En el Ejercicio 2, que implicaciones tiene para un sistema experto real
que se activen varias reglas a la vez**

Que se activen varias reglas simultaneamente refleja una situacion real:
un paciente puede tener mas de una condicion a la vez, o los sintomas
reportados pueden ser ambiguos y coincidir con varias enfermedades
distintas. Para un sistema experto real esto implica que se necesita una
estrategia clara de resolucion de conflictos (por ejemplo, asignar
salience o prioridad segun la gravedad de la enfermedad, pedir sintomas
adicionales para desambiguar, o presentar todos los diagnosticos posibles
ordenados por probabilidad en lugar de elegir uno solo). Tambien resalta la
importancia de que el sistema no se detenga en el primer diagnostico que
encuentre, sino que informe todas las hipotesis compatibles con la
evidencia, dejando la decision final a un profesional humano, especialmente
en un dominio de alto riesgo como el medico.
