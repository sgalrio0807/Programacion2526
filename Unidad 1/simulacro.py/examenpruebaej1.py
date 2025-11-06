incidente = input("¿Desea registrar un nuevo incidente? S (para Sí) o N (para No): ").lower()

while incidente == "s":
    nivel = input("¿En  qué nivel ha ocurrido? E (para los incidentes de ESO) y P (para los incidentes de Post-Obligatoria): ").lower()
    while nivel != "e" and nivel != "p":
        nivel = input("Nivel no válido, vuelve a introducir: E (para los incidentes de ESO) y P (para los incidentes de Post-Obligatoria): ").lower()
    tipoincidente= input("¿Qué tipo de incidente ha ocurrido?: , tipo de incidente: L ( para incidentes Leves)  o G (para incidentes Graves ): ").lower()
    while tipoincidente != "l" and tipoincidente != "g":
        tipoincidente= input("Tipo no válido, vuelve a introducir: tipo de incidente: L ( para incidentes Leves)  o G (para incidentes Graves ): ").lower()
    incidente = input("¿Desea registrar un nuevo incidente? S (para Sí) o N (para No): ").lower()

print("Incidentes registrados")