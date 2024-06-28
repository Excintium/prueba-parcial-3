
import json,os

# Agregar categoría:
# Al listado de categorías existente en el Json, agregamos al final de la lista la nueva categoría.
def agregar_categoria():
    with open('biblioteca.json', mode="r") as file:
        lectura = json.load(file)
        nueva_categoria = {
            "CategoriaID": len(lectura["Categoria"]) + 1,
            "Nombre":input('Ingrese el nombre de la nueva categoria: '),
        }
        lectura["Categoria"].append(nueva_categoria)
    with open('biblioteca.json', mode="w") as file:
        json.dump(lectura, file, indent=4)
        print("la categoria fue agregada!!!!")
        os.system("cls")

# # • Editar categoría
# Al listado de categorías en el Json, editamos la información (Nombre).
def editar_categoria():
    with open('biblioteca.json', mode="r") as file:
        lectura = json.load(file)
        idInput = int(input("ingrese la id de la categoria que desee modificar :"))
        for categoria in lectura["Categoria"]: 
            if categoria["CategoriaID"] == idInput:
                ID_categoria =(input("Ingresa el nuevo ID de la categoria: "))
                nombre_categoria =(input("Ingresa el nuevo nombre de la categoria: "))
                categoria["CategoriaID"]=ID_categoria
                categoria["Nombre"]=nombre_categoria
    with open("biblioteca.json", mode="w") as file:
        json.dump(lectura, file, indent=4) 
        print("La categoria fue editada!!!!")
        os.system("cls")




# • Eliminar categoría
# Al listado de categorías en el Json, eliminamos una categoría por su ID.
def eliminador_inador():
    with open("biblioteca.json", mode="r") as file:
        datos= json.load(file)
        id_buscada=input("Ingresa la id de la categoria a buscar: ")
        if id_buscada in datos["Categoria"]:
            del(datos["Categoria"][id_buscada])
    with open("biblioteca.json","w") as file:
        json.dump(datos, file, indent = 4)
        print("Categoria Eliminada")
        os.system("cls")



# • Buscar categoría
# Al listado de categorías en el Json, buscamos una categoría por su ID.
def buscar_categoria():
    with open('biblioteca.json', 'r') as file:
        datos_leidos = json.load(file)
        for categoria in datos_leidos["Categoria"]:
            print(categoria)


def menu_categorias():
    os.system("cls")
    print("1.- Agregar Categoria")
    print("2.- Editar Categoria")
    print("3.- Eliminar Categoria")
    print("4.- Buscar categoria")
    print("9.- Volver al menú principal")
    opc=int(input("ingresa tu opcion: "))
    if opc == 1:
        os.system("cls")
        agregar_categoria()
    elif opc == 2:
        os.system("cls")
        editar_categoria()
    elif opc == 3:
        os.system("cls")
        eliminador_inador()
    elif opc == 4:
        os.system("cls")
        buscar_categoria()



def reportes():
        with open("biblioteca.json",mode="r")as file:
            datos=json.load(file)
            prestamos=datos["Prestamo"]
            libros=datos["Libro"]

            prestamos_contador={}
            for prestamo in prestamos:
                libro_id=prestamo["LibroID"]
                if libro_id in prestamos_contador:
                    prestamos_contador[libro_id]+=1
                else:
                    prestamos_contador[libro_id]=1
            
            reporte=[]
            for libro in libros:
                titulo=libro["Titulo"]
                libro_id=libro["LibroID"]
                cantidad_prestamos=prestamos_contador.get(libro_id,0)
                reporte.append(titulo)
                reporte.append(cantidad_prestamos)
            for titulo in reporte:
                print(f"Libro:{titulo}")
            for cantidad in reporte:
                print(f"cantidad de veces prestado: {cantidad}")
