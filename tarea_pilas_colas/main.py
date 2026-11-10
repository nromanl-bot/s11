import os
from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


def limpiar_pantalla():
    """Limpia la consola tanto en Windows como en Mac/Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa la ejecución para que el usuario pueda leer el resultado antes de limpiar."""
    input("\n  [ Presiona Enter para continuar... ]")


# ------------------------- funciones de apoyo ✅ -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        limpiar_pantalla()
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 1. APILAR ] ---\n")
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print("\n  ✓ Apilado: ahora es el tope")
            pausar()
        elif op == "2":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 2. LISTAR PILA ] ---\n")
            pila.listar()
            pausar()
        elif op == "3":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 3. DESAPILAR ] ---\n")
            p = pila.desapilar()
            if p:
                print(f"  ✓ Salió: {p}")
            else:
                print("  ⚠ La pila está vacía")
            pausar()
        elif op == "4":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 4. VER TOPE ] ---\n")
            p = pila.ver_tope()
            if p:
                print(f"  Tope actual: {p}")
            else:
                print("  ⚠ La pila está vacía")
            pausar()
        elif op == "5":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 5. BUSCAR ] ---\n")
            num = leer_entero("  Ingrese n.º de pasajero a buscar: ")
            pos = pila.buscar(num)
            if pos != -1:
                print(f"  ✓ Encontrado en posición [{pos}]: {pila.datos[pos]}")
            else:
                print("  ❌ Pasajero no encontrado")
            pausar()
        elif op == "6":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 6. MODIFICAR ] ---\n")
            num = leer_entero("  N.º de pasajero a modificar: ")
            if pila.buscar(num) != -1:
                dest = input("  Nuevo destino: ").strip()
                asiento = input("  Nuevo asiento: ").strip().upper()
                if pila.modificar(num, dest, asiento):
                    print("  ✓ Pasajero modificado correctamente")
            else:
                print("  ❌ Pasajero no encontrado")
            pausar()
        elif op == "7":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 7. ELIMINAR POR NÚMERO ] ---\n")
            num = leer_entero("  N.º de pasajero a eliminar: ")
            if pila.eliminar_por_numero(num):
                print("  ✓ Pasajero eliminado respetando la pila")
            else:
                print("  ❌ Pasajero no encontrado o pila vacía")
            pausar()
        elif op == "8":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 8. COPIAR ] ---\n")
            copia = pila.copiar()
            print("  ✓ Copia realizada con éxito. Mostrando copia:")
            copia.listar()
            pausar()
        elif op == "9":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 9. LONGITUD / ¿VACÍA? ] ---\n")
            print(f"  Longitud actual: {pila.longitud()}")
            if pila.esta_vacia():
                print("  Estado: La pila está VACÍA")
            else:
                print("  Estado: La pila NO está vacía")
            pausar()
        elif op == "C":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: C. CARGAR DATOS DE PRUEBA ] ---\n")
            cargados = 0
            for p in datos_prueba():
                if pila.apilar(p):
                    cargados += 1
            print(f"  ✓ Datos de prueba procesados ({cargados} nuevos apilados)")
            pausar()
        elif op == "0":
            break
        else:
            print("  Opción no válida")
            pausar()


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        limpiar_pantalla()
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 1. ENCOLAR ] ---\n")
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print("\n  ✓ Encolado: está al final")
            pausar()
        elif op == "2":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 2. LISTAR COLA ] ---\n")
            cola.listar()
            pausar()
        elif op == "3":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 3. DESENCOLAR ] ---\n")
            p = cola.desencolar()
            if p:
                print(f"  ✓ Salió: {p}")
            else:
                print("  ⚠ La cola está vacía")
            pausar()
        elif op == "4":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 4. VER FRENTE ] ---\n")
            p = cola.ver_frente()
            if p:
                print(f"  Frente actual: {p}")
            else:
                print("  ⚠ La cola está vacía")
            pausar()
        elif op == "5":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 5. BUSCAR ] ---\n")
            num = leer_entero("  Ingrese n.º de pasajero a buscar: ")
            pos = cola.buscar(num)
            if pos != -1:
                print(f"  ✓ Encontrado en posición [{pos}]: {cola.datos[pos]}")
            else:
                print("  ❌ Pasajero no encontrado")
            pausar()
        elif op == "6":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 6. MODIFICAR ] ---\n")
            num = leer_entero("  N.º de pasajero a modificar: ")
            if cola.buscar(num) != -1:
                dest = input("  Nuevo destino: ").strip()
                asiento = input("  Nuevo asiento: ").strip().upper()
                if cola.modificar(num, dest, asiento):
                    print("  ✓ Pasajero modificado correctamente")
            else:
                print("  ❌ Pasajero no encontrado")
            pausar()
        elif op == "7":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 7. ELIMINAR POR NÚMERO ] ---\n")
            num = leer_entero("  N.º de pasajero a eliminar: ")
            if cola.eliminar_por_numero(num):
                print("  ✓ Pasajero eliminado respetando la cola")
            else:
                print("  ❌ Pasajero no encontrado o cola vacía")
            pausar()
        elif op == "8":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 8. COPIAR ] ---\n")
            copia = cola.copiar()
            print("  ✓ Copia realizada con éxito. Mostrando copia:")
            copia.listar()
            pausar()
        elif op == "9":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: 9. LONGITUD / ¿VACÍA? ] ---\n")
            print(f"  Longitud actual: {cola.longitud()}")
            if cola.esta_vacia():
                print("  Estado: La cola está VACÍA")
            else:
                print("  Estado: La cola NO está vacía")
            pausar()
        elif op == "C":
            limpiar_pantalla()
            print("--- [ OPCIÓN SELECCIONADA: C. CARGAR DATOS DE PRUEBA ] ---\n")
            cargados = 0
            for p in datos_prueba():
                if cola.encolar(p):
                    cargados += 1
            print(f"  ✓ Datos de prueba procesados ({cargados} nuevos encolados)")
            pausar()
        elif op == "0":
            break
        else:
            print("  Opción no válida")
            pausar()


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        limpiar_pantalla()
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            limpiar_pantalla()
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")
            pausar()


if __name__ == "__main__":
    main()
