'''Codigo básico para crear una calculadora usando funciones. Parte de formaciones realizadas en mi proceso
de aprendizaje de programación usando el lenguaje Python'''


def Sumar():
    Sum1 = int(input(" Introduzca el primer valor a sumar: "))
    Sum2 = int(input("Introduza el segundo valor  a sumar: "))
    print("La suma es: ", Sum1 + Sum2)
def Restar():
    Rest1 = int(input(" Introduzca el primer valor a restar: "))
    Rest2 = int(input("Introduza el segundo valor  a restar: "))
    print("La resta es: ", Rest1 - Rest2)
def Multiplicar():
    Mult1 = int(input(" Introduzca el primer valor a multiplicar: "))
    Mult2 = int(input("Introduza el segundo valor  a multiplicar: "))
    print("La multiplicación es: ", Mult1 * Mult2)
def Dividir():
    Div1 = int(input(" Introduzca el primer valor a dividir: "))
    Div2 = int(input("Introduza el segundo valor  a dividir: "))
    print("La división es: ", Div1 / Div2)
def Calculador():
    fin=False
    while not (fin):
        opc = int(input("Opcion: "))
        if (opc == 1):
            Sumar()
        elif (opc == 2):
            Restar()
        elif (opc == 3):
            Multiplicar()

        elif (opc == 4):
            Dividir()

        elif (opc == 5):
            fin = 1


print(""" ******Calculadora******
Menu
1) Suma
2) Resta
3) Mutiplicación
4) División
5) Salir""")
Calculador()