solicitante = (input("Ingrese su historial crediticio:"))
duracionempleo = float(input("Ingrese la duracion de su empleo en años:"))
cantidad = float(input("Ingrese porcentaje que solicita:"))

if solicitante == "negativo" and duracionempleo <= 2 and cantidad <= 1:
  print ("Considerado riesgo")
  
elif solicitante == "positivo" and duracionempleo >= 2 and cantidad >= 1:
  print ("Considerado no riesgo")