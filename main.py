
def multiplesOfThree():
    for _ in range(3, 100, 3):
        print(_)

def oddNumbers():
    for _ in range(1, 100, 2):
        print(_)

def pairNumbers():
    for _ in range(2, 101, 2):
        print(_)

def numbers():
    for _ in range(1, 4):
        print(_)

def inverted():
    for _ in range(10, 0, -1):
        print(_)

def squares():
    for _ in range(1, 31):
        print(math.pow(_, 2))

def sumSquares():
    sum = 0
    for _ in range(1, 101):
        sum += math.pow(_, 2)
    print(sum)

def sumFollowing(number):
    sum = 0
    for _ in range(number, (number + 101)):
        sum += _
    print(sum)

def factNumber(number):
    mult = 1
    for _ in range(1, (number+1)):
        mult *= _
    print(mult)

def temperature():
    while True:
        fahrenheit = float(input("Temp: "))
        if fahrenheit == 999:
            break
        celcius = (5 / 9) * (fahrenheit - 32)
        print(celcius)

def numPrimos(limit):
    for _ in range(2, (limit+1)):
        primo = True
        for i in range(2, int((math.sqrt(_))+1)):
            if _ % i == 0:
                primo = False
                break
        if primo:
            print(_)

def multiplicationTables(number):
    for _ in range(11):
        print(str(number) + " * " + str(_) + " = " + str(number*_))

def average():
    numbers = []

    while True:
        number = float(input("Enter the number: "))
        if number <= 0:
            break
        numbers.append(number)

    print("El promedio es ", (sum(numbers) / len(numbers)))

def numbers(number1, number2):
    if number1 == number2:
        print("Los numeros son iguales")
    elif number2 < number1:
        for _ in range(number2, (number1+1)):
            print(_)
    else:
        for _ in range(number1, (number2+1)):
            print(_)

def domino():
    for _ in range(7):
        for i in range(7):
            print("_________")
            print(f"| {_} | {i} |")
            print("¯¯¯¯¯¯¯¯¯")
