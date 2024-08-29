def mostrar_menu():
    mensaje = f"""
    ////////////////////MENÚ DE OPCIONES////////////////////
    |                                                      |
    |               1° VER SALDO :                         |
    |               2° REALIZAR DÉPOSITO :                 |
    |               3° REALIZAR UN RETIRO :                |
    |               4° SALIR :                             |
    |                                                      |
    ///////////////////////////////////////////////////////|
    """
    print(mensaje)
    
def mostrar_saldo(saldo):
    print(f"Su saldo actual es: {saldo}")

def deposito(saldo):
    deposito = int(input("Ingrese el monto a depositar :"))
    print("Depósito realizado con éxito:")
    saldo = deposito + saldo
    return saldo

def retiro(saldo):
    retiro = int(input("Ingrese el monto a retirar :"))
    if retiro >= saldo:
        print("Saldo insuficiente. No se puede realizar el retiro.")
    else:
        print("Retiro realizado con éxito.")
        saldo = saldo - retiro
    return saldo

def main():
    saldo = 0
    while True :
        mostrar_menu()
        usuario = int(input("Por favor ingresa tú opción con números :"))
        if usuario == 1 :
            mostrar_saldo(saldo)
        elif usuario == 2 :
            saldo = deposito(saldo)
        elif usuario == 3 :
            saldo = retiro(saldo)
        elif usuario == 4 :
            print("Gracias por utilizar nuestro servicio. ¡Hasta luego!.")
            exit()
        else :
            print("Por favor ingresa un número entre 1 y 4.")
main()