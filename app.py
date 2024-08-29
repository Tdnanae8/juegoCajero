def mostrar_menu():
    print("====== MENÚ PRINCIPAL ======")
    print("1. Saludar")
    print("2. Mostrar fecha y hora")
    print("3. Calcular la suma de dos números")
    print("4. Salir")
    print("=============================")

def saludar(nombre):
    
    mensaje = f"""
    ¡Hola! {nombre} ¿Cómo estás? 
"""
    print(mensaje)

def mostrar_fecha_hora():
    from datetime import datetime
    ahora = datetime.now()
    print("Fecha y hora actuales:", ahora.strftime("%Y-%m-%d %H:%M:%S"))

def calcular_suma():
    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        suma = numero1 + numero2
        print("La suma es:", suma)
    except ValueError:
        print("Por favor, introduce números válidos.")

def play():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            nombre = input("Dime tú nombre: ")
            saludar(nombre)
        elif opcion == '2':
            mostrar_fecha_hora()
        elif opcion == '3':
            calcular_suma()
        elif opcion == '4':
            print("¡Hasta luego!")
            exit()#funcion para salir del ciclo, al igual que break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

play()
