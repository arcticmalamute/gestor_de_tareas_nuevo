#agregar tareas, marcar completada, ver pendientes, ver completadas, salir

def mostra_menu():
    print("<----------------------------------------------->")
    print("bienvenido al menu, elija una de las 5 opciones")
    print("1. agregar tareas")
    print("2. marcar completada")
    print("3. ver pendientes ")
    print("4. ver completadas")
    print("5. salir")
    print("<----------------------------------------------->")


def agregar_tareas(lista_pendientes):
    try:
        cantidad = int(input("¿Cuántas tareas deseas agregar?: "))
        for _ in range(cantidad):
            tarea = input("Añada el nombre de la tarea: ")
            if tarea != "":
                lista_pendientes.append(tarea)
                print(f"La tarea: '{tarea}' se ha añadido correctamente")
            else:
                print("No ha colocado ninguna tarea")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

    return lista_pendientes


def marcar_completada(lista_pendientes, lista_completadas):
    tarea = input("Coloque el nombre de la tarea para marcarla completada: ")
    if tarea in lista_pendientes:
        lista_pendientes.remove(tarea)
        lista_completadas.append(tarea)
        print(f"La tarea '{tarea}' se ha marcado como completada.")
    else:
        print("Esa tarea no existe en pendientes.")

    return lista_pendientes, lista_completadas


continuar = "s"
completadas = []
pendientes = []

while continuar == "s":
    mostra_menu()
    menu = input("que desea hacer?: ")

    if menu == "agregar tareas" or menu == "1":
        pendientes = agregar_tareas(pendientes)

    elif menu == "marcar completada" or menu == "2":
        pendientes, completadas = marcar_completada(pendientes, completadas)

    elif menu == "ver pendientes" or menu == "3":
        for tarea in pendientes:
            print(f"tareas pendientes: {tarea}")

    elif menu == "ver completadas" or menu == "4":
        for tarea in completadas:
            print(f"tareas completadas: {tarea}")

    elif menu == "salir" or menu == "5":
        break

    continuar = input("deseas continuar? (s/n): ")

print("que tenga buen dia")