import json,os

from funciones2 import agregar_categoria,editar_categoria,eliminador_inador,buscar_categoria,menu_categorias,reportes

def menu_principal():
    while True:
        print("1.- Mantenedor de categorias")
        print("2.- Reportes")
        print("9.- Salir")
        opc=int(input("Ingresa tu opcion: "))
        os.system("cls")
        if opc == 1:
            menu_categorias()
        elif opc == 2:
            reportes()
        elif opc == 9:
            break

menu_principal()