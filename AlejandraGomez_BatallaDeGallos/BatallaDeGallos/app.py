from juego import Juego

if __name__ == "__main__":
    juego = Juego()  # Crea una instancia de la clase Juego
    opcion = juego.mostrar_inicio()  # Muestra el menú de inicio
    usr_name = " "
    if opcion == "1" or opcion == "2":  # Si la opción es 1 o 2
        usr_name = input("Ingrese su Nombre: ")  # Pide el nombre del usuario
        juego.iniciar_partida(opcion, usr_name)  # Inicia la partida
        juego.finalizar_ejecucion()  # Finaliza la ejecución
    else:
        juego.finalizar_ejecucion()  # Finaliza la ejecución
