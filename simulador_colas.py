"""
Proyecto: Simulación de un Sistema de Tareas en un Servidor mediante Colas y Bicolas
Descripción: Programa académico que simula la recepción y ejecución de 15 tareas
             en un servidor utilizando una Cola Simple (FIFO) para tareas normales
             y una Bicola (Deque) para tareas críticas.
"""

from collections import deque


class Tarea:
    """Representa una tarea que llega al servidor para ser procesada."""

    def __init__(self, id_tarea, descripcion, prioridad):
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.prioridad = prioridad  # "Normal" o "Crítica"


class ColaSimple:
    """
    Estructura de datos tipo Cola Simple (FIFO: First In, First Out).
    Las tareas se insertan al final y se extraen por el frente.
    """

    def __init__(self):
        self.elementos = deque()

    def encolar(self, tarea):
        """Inserta una tarea al final de la cola."""
        self.elementos.append(tarea)

    def desencolar(self):
        """Extrae y retorna la tarea ubicada al frente de la cola."""
        if not self.esta_vacia():
            return self.elementos.popleft()
        return None

    def esta_vacia(self):
        """Verifica si la cola no contiene elementos."""
        return len(self.elementos) == 0

    def tamano(self):
        """Retorna la cantidad actual de tareas en la cola."""
        return len(self.elementos)


class Bicola:
    """
    Estructura de datos tipo Bicola (Doble Cola / Deque).
    Permite insertar tareas críticas al inicio mediante appendleft()
    y extraerlas por el frente para su atención prioritaria.
    """

    def __init__(self):
        self.elementos = deque()

    def appendleft(self, tarea):
        """Inserta una tarea crítica al inicio (frente) de la bicola."""
        self.elementos.appendleft(tarea)

    def extraer_frente(self):
        """
        Extrae la tarea del frente de la bicola.
        Al insertar con appendleft() y extraer por el frente, se atiende
        inmediatamente la emergencia más reciente ingresada en la cabecera.
        """
        if not self.esta_vacia():
            return self.elementos.popleft()
        return None

    def esta_vacia(self):
        """Verifica si la bicola no contiene elementos."""
        return len(self.elementos) == 0

    def tamano(self):
        """Retorna la cantidad actual de tareas en la bicola."""
        return len(self.elementos)


def generar_tareas():
    """Genera y retorna una lista con exactamente 15 tareas predefinidas."""
    datos_tareas = [
        ("T-01", "Respaldo programado de archivos de usuario", "Normal"),
        ("T-02", "Alerta de intrusión en el cortafuegos principal", "Crítica"),
        ("T-03", "Actualización de índices de búsqueda interna", "Normal"),
        ("T-04", "Generación de reporte mensual de tráfico", "Normal"),
        ("T-05", "Caída del servicio de autenticación de usuarios", "Crítica"),
        ("T-06", "Limpieza de archivos temporales del sistema", "Normal"),
        ("T-07", "Sobrecarga de memoria en el nodo de base de datos", "Crítica"),
        ("T-08", "Sincronización de reloj del servidor con protocolo NTP", "Normal"),
        ("T-09", "Envío de boletín informativo por correo electrónico", "Normal"),
        ("T-10", "Fallo de lectura en el arreglo de discos RAID", "Crítica"),
        ("T-11", "Compresión de registros históricos de auditoría", "Normal"),
        ("T-12", "Verificación de espacio libre en particiones secundarias", "Normal"),
        ("T-13", "Pérdida de conectividad con la pasarela de pagos", "Crítica"),
        ("T-14", "Escaneo rutinario de permisos de carpetas compartidas", "Normal"),
        ("T-15", "Intento de acceso no autorizado al panel raíz (root)", "Crítica"),
    ]

    lista_tareas = []
    for id_tarea, descripcion, prioridad in datos_tareas:
        nueva_tarea = Tarea(id_tarea, descripcion, prioridad)
        lista_tareas.append(nueva_tarea)

    return lista_tareas


def recibir_tareas(lista_tareas, cola_normales, bicola_criticas):
    """
    Registra la llegada de las tareas al servidor y las clasifica
    en la estructura correspondiente según su nivel de prioridad.
    """
    print("=" * 95)
    print("SIMULACIÓN DE UN SISTEMA DE TAREAS EN UN SERVIDOR MEDIANTE COLAS Y BICOLAS")
    print("=" * 95)
    print("\n1. REGISTRO DE LLEGADA DE TAREAS AL SERVIDOR\n")
    print(f"{'ID':<6} | {'Prioridad':<9} | {'Estructura Asignada':<26} | {'Descripción'}")
    print("-" * 95)

    for tarea in lista_tareas:
        if tarea.prioridad == "Crítica":
            # Se inserta al inicio de la bicola usando appendleft()
            bicola_criticas.appendleft(tarea)
            estructura_usada = "Bicola (appendleft)"
        else:
            # Se inserta al final de la cola simple respetando FIFO
            cola_normales.encolar(tarea)
            estructura_usada = "Cola Simple (FIFO)"

        print(
            f"{tarea.id_tarea:<6} | {tarea.prioridad:<9} | "
            f"{estructura_usada:<26} | {tarea.descripcion}"
        )


def procesar_tareas(cola_normales, bicola_criticas):
    """
    Ejecuta primero todas las tareas críticas almacenadas en la bicola
    y posteriormente todas las tareas normales almacenadas en la cola simple.
    """
    print("\n" + "=" * 95)
    print("2. ORDEN PASO A PASO DE EJECUCIÓN EN EL SERVIDOR")
    print("=" * 95)

    tareas_ejecutadas = []
    contador_criticas = 0
    contador_normales = 0
    paso_actual = 1

    # Fase 1: Procesamiento prioritario de tareas críticas desde la Bicola
    print("\n--- Fase A: Procesando Tareas Críticas (Bicola - Extracción desde el frente) ---")
    while not bicola_criticas.esta_vacia():
        tarea_actual = bicola_criticas.extraer_frente()
        tareas_ejecutadas.append(tarea_actual)
        contador_criticas += 1
        print(
            f"Paso {paso_actual:02d} -> [EJECUTANDO] ID: {tarea_actual.id_tarea} | "
            f"Prioridad: {tarea_actual.prioridad:<7} | Origen: Bicola      | "
            f"Tarea: {tarea_actual.descripcion}"
        )
        paso_actual += 1

    # Fase 2: Procesamiento de tareas normales desde la Cola Simple (FIFO)
    print("\n--- Fase B: Procesando Tareas Normales (Cola Simple - Orden de llegada FIFO) ---")
    while not cola_normales.esta_vacia():
        tarea_actual = cola_normales.desencolar()
        tareas_ejecutadas.append(tarea_actual)
        contador_normales += 1
        print(
            f"Paso {paso_actual:02d} -> [EJECUTANDO] ID: {tarea_actual.id_tarea} | "
            f"Prioridad: {tarea_actual.prioridad:<7} | Origen: Cola Simple | "
            f"Tarea: {tarea_actual.descripcion}"
        )
        paso_actual += 1

    return tareas_ejecutadas, contador_criticas, contador_normales


def validar_y_mostrar_resumen(
    tareas_generadas,
    tareas_ejecutadas,
    total_criticas,
    total_normales,
    cola_normales,
    bicola_criticas,
):
    """
    Valida que se hayan procesado exactamente 15 tareas sin pérdidas ni
    duplicaciones, comprueba que las estructuras hayan quedado vacías
    y muestra el resumen final de la simulación.
    """
    total_generadas = len(tareas_generadas)
    total_procesadas = len(tareas_ejecutadas)

    # Conjunto de identificadores para verificar pérdidas o duplicados
    ids_generados = [t.id_tarea for t in tareas_generadas]
    ids_ejecutados = [t.id_tarea for t in tareas_ejecutadas]

    sin_duplicados = len(ids_ejecutados) == len(set(ids_ejecutados))
    sin_perdidas = set(ids_generados) == set(ids_ejecutados)
    cantidad_correcta = total_procesadas == 15
    estructuras_vacias = cola_normales.esta_vacia() and bicola_criticas.esta_vacia()

    print("\n" + "=" * 95)
    print("3. RESUMEN FINAL Y VALIDACIÓN DEL SISTEMA")
    print("=" * 95)
    print(f"• Cantidad de tareas críticas procesadas : {total_criticas}")
    print(f"• Cantidad de tareas normales procesadas : {total_normales}")
    print(f"• Total de tareas generadas inicialmente : {total_generadas}")
    print(f"• Total de tareas procesadas por servidor: {total_procesadas}")
    print("-" * 95)
    print(f"• Estado final de la Bicola (Críticas)   : {'Vacía (0 elementos)' if bicola_criticas.esta_vacia() else 'Con elementos pendientes'}")
    print(f"• Estado final de la Cola (Normales)     : {'Vacía (0 elementos)' if cola_normales.esta_vacia() else 'Con elementos pendientes'}")
    print("-" * 95)

    if cantidad_correcta and sin_duplicados and sin_perdidas and estructuras_vacias:
        print(
            "CONFIRMACIÓN EXITOSA: Se procesaron exactamente las 15 tareas programadas.\n"
            "Todas las tareas fueron ejecutadas sin pérdidas ni duplicaciones, y ambas\n"
            "estructuras de datos quedaron completamente vacías al finalizar."
        )
    else:
        print(
            "ADVERTENCIA DE VALIDACIÓN: Se detectó una inconsistencia en el procesamiento."
        )
    print("=" * 95)


def ejecutar_simulacion():
    """Función principal que coordina toda la simulación del servidor."""
    # Inicialización de las estructuras de datos
    cola_tareas_normales = ColaSimple()
    bicola_tareas_criticas = Bicola()

    # 1. Generación de las 15 tareas
    lista_tareas = generar_tareas()

    # 2. Recepción y almacenamiento en la estructura correspondiente
    recibir_tareas(lista_tareas, cola_tareas_normales, bicola_tareas_criticas)

    # 3. Ejecución ordenada (primero críticas, después normales)
    tareas_ejecutadas, total_criticas, total_normales = procesar_tareas(
        cola_tareas_normales, bicola_tareas_criticas
    )

    # 4. Validación final y reporte de resultados
    validar_y_mostrar_resumen(
        lista_tareas,
        tareas_ejecutadas,
        total_criticas,
        total_normales,
        cola_tareas_normales,
        bicola_tareas_criticas,
    )


if __name__ == "__main__":
    ejecutar_simulacion()