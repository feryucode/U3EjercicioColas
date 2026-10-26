class Nodo:
    def __init__(self, info=None):
        self.INFO = info
        self.LIGA = None


class LinkedList:
    def __init__(self):
        self.P = None
        self.ramas_externas = []

    def esta_vacia(self):
        return self.P is None

    def crea_inicio(self):
        self.P = Nodo()
        self.P.INFO = input("Ingrese el dato del primer nodo (P^.INFO): ")
        self.P.LIGA = None

        RES = int(input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 -> "))
        while RES == 1:
            Q = Nodo()
            Q.INFO = input("Ingrese el dato del nuevo nodo (Q^.INFO): ")
            Q.LIGA = self.P
            self.P = Q
            RES = int(input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 -> "))
        print("Lista inicial creada con éxito.")

    def recorrido(self):
        if self.P is None:
            print("La lista está vacía (P = NIL).")
            return

        Q = self.P
        nodos = []
        visitados = set()
        ciclo = False

        while Q is not None:
            if id(Q) in visitados:
                nodos.append(f"🔄 [CICLO hacia '{Q.INFO}']")
                ciclo = True
                break
            visitados.add(id(Q))
            nodos.append(f"[{Q.INFO}]")
            Q = Q.LIGA

        fin = "" if ciclo else " -> NIL"
        print("P -> " + " -> ".join(nodos) + fin)

        if self.ramas_externas:
            for i, ext in enumerate(self.ramas_externas, 1):
                dest = ext.LIGA.INFO if ext.LIGA else "NIL"
                print(f"   └── Rama externa {i}: [{ext.INFO}] -> apunta a [{dest}]")

    def inserta_inicio(self, DATO):
        Q = Nodo(DATO)
        Q.LIGA = self.P
        self.P = Q
        print(f"Nodo '{DATO}' insertado al inicio.")

    def inserta_final(self, DATO):
        Q = Nodo(DATO)
        if self.P is None:
            self.P = Q
        else:
            T = self.P
            while T.LIGA is not None:
                T = T.LIGA
            T.LIGA = Q
        print(f"Nodo '{DATO}' insertado al final.")

    def inserta_antes_x(self, DATO, X):
        if self.P is None:
            print("La lista está vacía.")
            return

        Q = self.P
        T = None
        BAND = 1

        while (Q.INFO != X) and (BAND == 1):
            if Q.LIGA is not None:
                T = Q
                Q = Q.LIGA
            else:
                BAND = 0

        if BAND == 1:
            NUEVO = Nodo(DATO)
            if self.P == Q:
                NUEVO.LIGA = self.P
                self.P = NUEVO
            else:
                T.LIGA = NUEVO
                NUEVO.LIGA = Q
            print(f"Nodo '{DATO}' insertado ANTES de '{X}'.")
        else:
            print(f"El nodo referencia '{X}' no se encuentra en la lista.")

    def inserta_despues_x(self, DATO, X):
        if self.P is None:
            print("La lista está vacía.")
            return

        Q = self.P
        BAND = 1

        while (Q.INFO != X) and (BAND == 1):
            if Q.LIGA is not None:
                Q = Q.LIGA
            else:
                BAND = 0

        if BAND == 1:
            T = Nodo(DATO)
            T.LIGA = Q.LIGA
            Q.LIGA = T
            print(f"Nodo '{DATO}' insertado DESPUÉS de '{X}'.")
        else:
            print(f"El nodo referencia '{X}' no se encuentra en la lista.")

    def elimina_inicio(self):
        if self.P is None:
            print("La lista está vacía.")
        else:
            Q = self.P
            self.P = Q.LIGA
            print(f"Primer nodo ('{Q.INFO}') eliminado.")
            del Q

    def elimina_ultimo(self):
        if self.P is None:
            print("La lista está vacía.")
        else:
            Q = self.P
            if self.P.LIGA is None:
                self.P = None
            else:
                T = None
                while Q.LIGA is not None:
                    T = Q
                    Q = Q.LIGA
                T.LIGA = None
            print(f"Último nodo ('{Q.INFO}') eliminado.")
            del Q

    def elimina_x(self, X):
        if self.P is None:
            print("La lista está vacía.")
            return

        Q = self.P
        T = None
        BAND = 1

        while (Q.INFO != X) and (BAND == 1):
            if Q.LIGA is not None:
                T = Q
                Q = Q.LIGA
            else:
                BAND = 0

        if BAND == 0:
            print(f"El elemento '{X}' no está en la lista.")
        else:
            if self.P == Q:
                self.P = Q.LIGA
            else:
                T.LIGA = Q.LIGA
            print(f"Nodo '{X}' eliminado.")
            del Q

    def elimina_antes_x(self, X):
        if self.P is None:
            print("La lista está vacía.")
            return

        if self.P.INFO == X:
            print(f"No existe un nodo anterior a '{X}' (es el primero).")
        else:
            Q = self.P
            T = self.P
            R = None
            BAND = 1

            while (Q.INFO != X) and (BAND == 1):
                if Q.LIGA is not None:
                    R = T
                    T = Q
                    Q = Q.LIGA
                else:
                    BAND = 0

            if BAND == 0:
                print(f"El elemento '{X}' no se encuentra en la lista.")
            else:
                if self.P.LIGA == Q:
                    self.P = Q
                else:
                    R.LIGA = Q
                print(f"Nodo '{T.INFO}' (anterior a '{X}') eliminado.")
                del T

    def buscar_nodo_objeto(self, X):
        Q = self.P
        visitados = set()
        while Q is not None and id(Q) not in visitados:
            if Q.INFO == X:
                return Q
            visitados.add(id(Q))
            Q = Q.LIGA
        return None

    def buscar(self, X):
        nodo = self.buscar_nodo_objeto(X)
        if nodo is None:
            print(f"El elemento '{X}' NO se encuentra en la lista.")
            return False
        else:
            print(f"El elemento '{X}' SÍ se encuentra en la lista.")
            return True

    def apuntar_dos_a_uno(self, dato_nuevo, dato_objetivo):
        objetivo = self.buscar_nodo_objeto(dato_objetivo)
        if objetivo is None:
            print(f"No existe el nodo '{dato_objetivo}'.")
            return
        nuevo = Nodo(dato_nuevo)
        nuevo.LIGA = objetivo
        self.ramas_externas.append(nuevo)
        print(f"Ahora el nuevo nodo ['{dato_nuevo}'] también apunta a ['{dato_objetivo}'].")