import MyLinkedList

def ejecutar_programa():
    lista = MyLinkedList.LinkedList()

    while True:
        print("\n==================================================")
        print("   PROBANDO BIBLIOTECA: MyLinkedList (ADA4)       ")
        print("==================================================")
        print("1. Crear lista al inicio (Algoritmo 5.1 Crea_inicio)")
        print("2. Recorrido de la lista")
        print("3. Insertar un elemento (5.2.3)")
        print("4. Borrar un elemento   (5.2.4)")
        print("5. Buscar un elemento   (5.2.5)")
        print("6. Hacer que 2 nodos apunten a un mismo nodo")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            lista.crea_inicio()

        elif opcion == "2":
            lista.recorrido()

        elif opcion == "3":
            print("\n--- OPCIONES DE INSERCIÓN ---")
            print("a) Insertar al inicio")
            print("b) Insertar al final")
            print("c) Insertar ANTES de un elemento X")
            print("d) Insertar DESPUÉS (delante) de un elemento X")
            sub = input("Elija opción (a/b/c/d): ").lower()
            dato = input("Ingrese el nuevo dato (INFO): ")

            if sub == "a":
                lista.inserta_inicio(dato)
            elif sub == "b":
                lista.inserta_final(dato)
            elif sub == "c":
                x = input("¿ANTES de qué elemento (X) lo quiere poner?: ")
                lista.inserta_antes_x(dato, x)
            elif sub == "d":
                x = input("¿DESPUÉS (delante) de qué elemento (X) lo quiere poner?: ")
                lista.inserta_despues_x(dato, x)

        elif opcion == "4":
            print("\n--- OPCIONES DE BORRADO ---")
            print("a) Eliminar el primer nodo")
            print("b) Eliminar el último nodo")
            print("c) Eliminar un nodo con información X")
            print("d) Eliminar el nodo ANTERIOR a X")
            sub = input("Elija opción (a/b/c/d): ").lower()

            if sub == "a":
                lista.elimina_inicio()
            elif sub == "b":
                lista.elimina_ultimo()
            elif sub == "c":
                x = input("Ingrese el dato (X) a eliminar: ")
                lista.elimina_x(x)
            elif sub == "d":
                x = input("¿Eliminar el nodo anterior a cuál elemento (X)?: ")
                lista.elimina_antes_x(x)

        elif opcion == "5":
            x = input("Ingrese el dato (X) que desea buscar: ")
            lista.buscar(x)

        elif opcion == "6":
            nuevo = input("Dato del nuevo nodo: ")
            objetivo = input("¿A qué nodo existente quiere que apunte?: ")
            lista.apuntar_dos_a_uno(nuevo, objetivo)

        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar_programa()