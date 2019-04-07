class Calculator:

    """Constructor of Calculator class"""
    def __init__(self):
        self.__numbers = [0,0]
    
    """Let the user introduce the numbers"""
    def askForNumbers(self):
        try:
            number0 = float(input("Introduce first number: "))
            number1 = float(input("Introduce second number: "))
            self.__numbers[0] = number0
            self.__numbers[1] = number1
            return 1
        except Exception:
            print("ask")
            return 0

    """Obtain the result of the chosen option"""
    def getResult(self,option):
        if option != 4:
            return [{
                1: self.__numbers[0] + self.__numbers[1],
                2: self.__numbers[0] - self.__numbers[1],
                3: self.__numbers[0] * self.__numbers[1],
                5: self.__numbers[0]**self.__numbers[1]
            }.get(option),1]
        else:
            try:
                return [self.__numbers[0] / self.__numbers[1], 1]
            except ZeroDivisionError:
                return [1,0]

        
"""Show the menu"""
def menu():
    print("1.Sum\n2.Substraction\n3.Multiplication\n4.Division\n5.Power\nAny for exit")
    
"""Let the user choose an option"""
def chooseInMenu():
    try:
        return int(input("Please, choose an option: "))
    except Exception:
        return -1
    except KeyboardInterrupt:
        return -1
