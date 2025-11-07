incidente = input("¿Desea registrar un nuevo incidente? S (para Sí) o N (para No): ").lower()
incidentes = 0
leves = 0
graves = 0
eso = 0
post = 0

while incidente == "s":
    incidentes += 1
    nivel = input("¿En  qué nivel ha ocurrido? E (para los incidentes de ESO) y P (para los incidentes de Post-Obligatoria): ").lower()
    if nivel == "e":
        eso += 1
    elif nivel == "p":
        post += 1
    while nivel != "e" and nivel != "p":
        nivel = input("Nivel no válido, vuelve a introducir: E (para los incidentes de ESO) y P (para los incidentes de Post-Obligatoria): ").lower()
    tipoincidente= input("¿Qué tipo de incidente ha ocurrido?: , tipo de incidente: L ( para incidentes Leves)  o G (para incidentes Graves ): ").lower()
    if tipoincidente == "l":
        leves += 1
    elif tipoincidente == "g":
        graves += 1
    while tipoincidente != "l" and tipoincidente != "g":
        tipoincidente= input("Tipo no válido, vuelve a introducir: tipo de incidente: L ( para incidentes Leves)  o G (para incidentes Graves ): ").lower()
    incidente = input("¿Desea registrar un nuevo incidente? S (para Sí) o N (para No): ").lower()

if incidentes > 0:
    porcentaje_eso = (eso / incidentes) * 100
    porcentaje_post = (post / incidentes) * 100
    print("Se han producido", incidentes, "incidentes en el centro:", leves, "de ellos Leves y", graves, "de ellos graves, siendo el", porcentaje_eso, "% en ESO y el", porcentaje_post, "% en Post-Obligatoria.")

else:
    print("Ninguna incidencia registrada.")