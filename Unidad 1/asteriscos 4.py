num= int(input("Dime un numero: "))
for numfila in range(num):
    if numfila == 0 or numfila == num -1:
        print("*   *")
    else:
        print("*****")
