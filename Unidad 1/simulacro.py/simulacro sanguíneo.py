donante= input("Dime un grupo sanguíneo(A, B, AB, 0): ")
receptor= input("Dime otro grupo sanguíneo(A, B, AB, 0): ")

match donante :
    case "0": 
        print("Los grupos son compatibles, el receptor puede recibir sangre de 0.")
    case "A":
        if receptor == "A" or receptor == "AB":
            print("Los grupos sanguíneos son compatibles, el receptor puede recibir sangre de A.")
        else: 
            print("Los grupos sanguíneos no son compatoibles, el receptor no puede recibir sangre de A.")
    case "B":
        if receptor == "B" or receptor == "AB":
            print("Los grupos sanguíneos son compatibles, el receptor puede recibir sangre de B.")
        else: 
            print("Los grupos sanguíneos no son compatoibles, el receptor no puede recibir sangre de B.")
    case "AB":
        if receptor == "Ab":
            print("Los grupos sanguíneos son compatibles, el receptor puede recibir sangre de AB.")
        else: 
            print("Los grupos sanguíneos no son compatoibles, el receptor no puede recibir sangre de AB.")