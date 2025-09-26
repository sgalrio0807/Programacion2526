print("Introduce temperatura")
temperatura = float (input())
if temperatura >26 :
    print("Enciendo el aire")
elif temperatura <10 :
    print("Enciendo la calefacción")
else:
      print("Apagar todo")
print("Registro"+ str (temperatura))