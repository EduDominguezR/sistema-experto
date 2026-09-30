"""
sistema_experto.py

Sistema experto de diagnostico medico simple, implementado con la libreria
`experta` (fork mantenido de pyknow), usando encadenamiento hacia adelante
(forward chaining).
"""

from experta import Fact, KnowledgeEngine, Rule, NOT


class Sintoma(Fact):
    """Representa un sintoma presente en el paciente.

    Se instancia con atributos booleanos con nombre, por ejemplo:
    Sintoma(fiebre=True, tos=True)
    Cada atributo indica si ese sintoma especifico esta presente (True)
    o no (False) en la memoria de trabajo del motor.
    """
    pass


class Diagnostico(Fact):
    """Representa un diagnostico generado por el motor de inferencia.

    Almacena el nombre de la enfermedad identificada, por ejemplo:
    Diagnostico(enfermedad="Gripe")
    Cuando se declara este hecho, indica que alguna regla del sistema
    encontro una combinacion de sintomas que coincide con una enfermedad.
    """
    pass


class SistemaDiagnostico(KnowledgeEngine):
    """Motor de inferencia con las reglas de diagnostico medico."""

    # ---------- Reglas originales (Parte 2) ----------

    @Rule(Sintoma(fiebre=True), Sintoma(tos=True), Sintoma(dolor_garganta=True))
    def diagnostico_gripe(self):
        self.declare(Diagnostico(enfermedad="Gripe"))
        print("Diagnostico: Gripe")
        print("Recomendacion: Reposo, hidratacion abundante y "
              "paracetamol para la fiebre. Consultar a un medico si "
              "los sintomas persisten mas de una semana.")

    @Rule(Sintoma(fiebre=True), Sintoma(dolor_cabeza=True), Sintoma(nauseas=True))
    def diagnostico_migrana(self):
        self.declare(Diagnostico(enfermedad="Migrana"))
        print("Diagnostico: Migrana")
        print("Recomendacion: Descansar en un lugar oscuro y silencioso, "
              "evitar pantallas y consultar a un medico si el dolor es "
              "muy intenso o recurrente.")

    @Rule(Sintoma(estornudos=True), Sintoma(congestion_nasal=True), Sintoma(picazon_ojos=True))
    def diagnostico_alergia(self):
        self.declare(Diagnostico(enfermedad="Alergia"))
        print("Diagnostico: Alergia")
        print("Recomendacion: Evitar el alergeno sospechoso, considerar "
              "un antihistaminico y consultar a un alergologo si los "
              "sintomas son frecuentes.")

    @Rule(Sintoma(dolor_estomago=True), Sintoma(diarrea=True), Sintoma(vomitos=True))
    def diagnostico_gastroenteritis(self):
        self.declare(Diagnostico(enfermedad="Gastroenteritis"))
        print("Diagnostico: Gastroenteritis")
        print("Recomendacion: Mantener buena hidratacion con sales "
              "orales, dieta blanda y consultar a un medico si hay "
              "signos de deshidratacion o fiebre alta.")

    # ---------- Ejercicio 1: nuevas reglas ----------

    @Rule(Sintoma(fiebre=True), Sintoma(tos_seca=True), Sintoma(perdida_olfato=True))
    def diagnostico_covid(self):
        self.declare(Diagnostico(enfermedad="COVID-19"))
        print("Diagnostico: COVID-19")
        print("Recomendacion: Aislarse, hacerse una prueba y contactar "
              "a un medico, especialmente si hay dificultad para "
              "respirar.")

    @Rule(Sintoma(congestion_nasal=True), Sintoma(estornudos=True), Sintoma(tos_leve=True))
    def diagnostico_resfriado(self):
        self.declare(Diagnostico(enfermedad="Resfriado comun"))
        print("Diagnostico: Resfriado comun")
        print("Recomendacion: Descanso, liquidos calientes y "
              "descongestionantes de venta libre; suele resolverse en "
              "pocos dias.")

    @Rule(Sintoma(tos_persistente=True), Sintoma(flema=True), Sintoma(dificultad_respiratoria=True))
    def diagnostico_bronquitis(self):
        self.declare(Diagnostico(enfermedad="Bronquitis"))
        print("Diagnostico: Bronquitis")
        print("Recomendacion: Evitar irritantes como el humo, mantenerse "
              "hidratado y consultar a un medico si la dificultad "
              "respiratoria empeora.")

    @Rule(Sintoma(dolor_articular=True), Sintoma(sarpullido=True), Sintoma(fiebre=True))
    def diagnostico_dengue(self):
        self.declare(Diagnostico(enfermedad="Dengue"))
        print("Diagnostico: Dengue")
        print("Recomendacion: Buscar atencion medica de inmediato, "
              "evitar aspirina/ibuprofeno y vigilar signos de alarma "
              "como sangrado o dolor abdominal intenso.")

    # ---------- Regla de respaldo (Parte 2, punto 5) ----------

    @Rule(NOT(Diagnostico()))
    def sin_diagnostico(self):
        print("Diagnostico: No se pudo determinar un diagnostico.")
        print("Recomendacion: Consultar a un medico para una "
              "evaluacion mas detallada.")
