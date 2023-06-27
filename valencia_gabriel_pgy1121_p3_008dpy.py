import numpy as np
import funciones_pru as fun

lista_rut=[]
lista_nombre=[]
lista_nombre_mascota=[]
lista_dias=[]
lista_identificador=[]
lista_pisos=[]
lista_salas=[]

largo=2
ancho=5

lista = np.zeros((largo,ancho),int)

contador_1=0

while True:
    print("""MENU MASCOTA SEGURA
    1.Grabar
    2.buscar
    3.retirarse
    4.salir""")
    opciones = fun.validar_opcion()
    if opciones == 1:
        ruts=fun.validar_rut()
        nombre=fun.validar_nombre()
        nombre_mascota=fun.validar_nombre_mascota()
        dias=fun.validar_dias()
        
        print("\tVER HABITACIONES\n")
        contador = 1
        for x in range(largo):
            print(f"piso:{(x+1)} //",end=" ") #parte inicial
            for y in range(ancho):
                print(f"sala {contador}: {lista[x][y]} ", end=" ") #filas y hileras 
                contador += 1
            print("\n")

        print("Escojer habitacion:")
        while True:
            try:
                piso = int(input("Ingrese piso que desea: "))
                if piso in (1,2):
                    break
                else:
                    print("ERROR! EL RUT DEBE SER MAYOR O IGUAL A 0!")
            except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
        while True:
            try:
                sala = int(input("Ingrese habitacion que desea: "))
                if sala >= 1 and sala <=10:
                    break
                else:
                    print("ERROR! EL RUT DEBE SER MAYOR O IGUAL A 0!")
            except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
        piso=piso-1

        if piso==1 and sala>=6:
            sala=sala-6
        else:
            sala=sala-1

        if lista[piso][sala] == 1:
            print("error debe ingrear denuevo los datos en una sala difernte")
        else:
            lista [piso][sala] = 1
            contador_1=contador_1+1
            lista_dias.append(dias)
            lista_identificador.append(contador_1)
            lista_nombre.append(nombre)
            lista_nombre_mascota.append(nombre_mascota)
            lista_rut.append(ruts)   
            lista_pisos.append(piso)
            lista_salas.append(sala)
            print("ingreso exitoso!!")

        print("\tVER HABITACIONES\n")
        contador = 1
        for x in range(largo):
            print(f"piso:{(x+1)} //",end=" ") #parte inicial
            for y in range(ancho):
                print(f"sala {contador}: {lista[x][y]} ", end=" ") #filas y hileras 
                contador += 1
            print("\n")    
  

    elif opciones == 2:
        rut=int(input("ingrese rut"))
        if rut in lista_rut:
            for x in range(len(lista_rut)):
                if rut == lista_rut[x]:
                    posicion=x
        else:
            print("su rut no se encuentra registrado")
        print(f"su mascota {lista_nombre_mascota[posicion]} esta en el piso {lista_pisos[posicion]+1}, en la sala {lista_salas[posicion]+1}")



    elif opciones==3:
        rut=int(input("ingrese rut"))
        if rut in lista_rut:
            for x in range(len(lista_rut)):
                if rut == lista_rut[x]:
                    posicion=x
        else:
            print("su rut no se encuentra registrado")

        total=lista_dias[posicion]*15000    
        print(f"su total a pagar es de ${total} con {lista_dias[posicion]} dias")
    else:
        print("gracias por escojer nuestro holtel para perros")
        break



