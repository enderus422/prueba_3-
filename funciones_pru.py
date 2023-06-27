import numpy

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")     

def validar_nombre_mascota():
    while True:
        nombre = input("Ingrese nombre mascota: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")                

def validar_dias():
    while True:
        try:
            dias = int(input("Ingrese la cantidad de dias a quedarse: "))
            if dias >= 0:
                return dias
            else:
                print("ERROR! EL RUT DEBE SER MAYOR O IGUAL A 0!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

