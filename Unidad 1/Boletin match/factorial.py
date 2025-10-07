num= int(input("Dame un numero:"))
fac= num
for numVeces in range(num, 0, -1) :
    print(numVeces, "*", fac)
    fac = fac * numVeces
    print(fac)
print("fin")

