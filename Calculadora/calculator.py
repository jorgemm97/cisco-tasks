from calculatorAux import menu,chooseInMenu,Calculator

"Create an object of Calculator class"
calcObj = Calculator()

menu()
option = chooseInMenu()

while option in range(1,6):
    boolValue = calcObj.askForNumbers()
    result = calcObj.getResult(option)
    if result[1] and boolValue:
        print("The result is: ",str(result[0]))
        menu()
        option = chooseInMenu()
    else:
        print("A strange thing happened. Please, try again...")
        option = chooseInMenu()

print("See you soon")