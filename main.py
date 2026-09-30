"""
main.py

Ejecuta los casos de prueba de la Parte 3, ademas de casos adicionales para
las enfermedades agregadas en el Ejercicio 1 y el conflicto de reglas del
Ejercicio 2.
"""

from sistema_experto import SistemaDiagnostico, Sintoma


def ejecutar_caso(titulo, sintomas):
    print("=" * 60)
    print(titulo)
    print("-" * 60)
    engine = SistemaDiagnostico()
    engine.reset()
    for sintoma in sintomas:
        engine.declare(sintoma)
    engine.run()
    print()


if __name__ == "__main__":
    # ---------- Parte 3: casos de prueba ----------

    ejecutar_caso(
        "Caso 1: fiebre, tos y dolor de garganta",
        [Sintoma(fiebre=True), Sintoma(tos=True), Sintoma(dolor_garganta=True)],
    )

    ejecutar_caso(
        "Caso 2: estornudos, congestion nasal y picazon en los ojos",
        [Sintoma(estornudos=True), Sintoma(congestion_nasal=True), Sintoma(picazon_ojos=True)],
    )

    ejecutar_caso(
        "Caso 3: dolor de estomago, diarrea y vomitos",
        [Sintoma(dolor_estomago=True), Sintoma(diarrea=True), Sintoma(vomitos=True)],
    )

    ejecutar_caso(
        "Caso 4: cansancio y mareo (sin regla que coincida)",
        [Sintoma(cansancio=True), Sintoma(mareo=True)],
    )

    ejecutar_caso(
        "Caso 5: fiebre, tos, dolor de garganta, estornudos y congestion nasal (activa mas de una regla)",
        [
            Sintoma(fiebre=True),
            Sintoma(tos=True),
            Sintoma(dolor_garganta=True),
            Sintoma(estornudos=True),
            Sintoma(congestion_nasal=True),
        ],
    )

    # ---------- Ejercicio 1: pruebas de las nuevas enfermedades ----------

    ejecutar_caso(
        "Caso 6 (Ejercicio 1): fiebre, tos seca y perdida de olfato -> COVID-19",
        [Sintoma(fiebre=True), Sintoma(tos_seca=True), Sintoma(perdida_olfato=True)],
    )

    ejecutar_caso(
        "Caso 7 (Ejercicio 1): congestion nasal, estornudos y tos leve -> Resfriado comun",
        [Sintoma(congestion_nasal=True), Sintoma(estornudos=True), Sintoma(tos_leve=True)],
    )

    ejecutar_caso(
        "Caso 8 (Ejercicio 1): tos persistente, flema y dificultad respiratoria -> Bronquitis",
        [Sintoma(tos_persistente=True), Sintoma(flema=True), Sintoma(dificultad_respiratoria=True)],
    )

    ejecutar_caso(
        "Caso 9 (Ejercicio 1): dolor articular, sarpullido y fiebre -> Dengue",
        [Sintoma(dolor_articular=True), Sintoma(sarpullido=True), Sintoma(fiebre=True)],
    )

    # ---------- Ejercicio 2: conflicto de reglas ----------

    ejecutar_caso(
        "Caso 10 (Ejercicio 2): sintomas de gripe y alergia a la vez",
        [
            Sintoma(fiebre=True),
            Sintoma(tos=True),
            Sintoma(dolor_garganta=True),
            Sintoma(estornudos=True),
            Sintoma(congestion_nasal=True),
            Sintoma(picazon_ojos=True),
        ],
    )
