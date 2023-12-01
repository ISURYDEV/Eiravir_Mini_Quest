from characters.player import Warrior, Mage, Archer



def create_player():
    print("\n¡Bienvenido aventurero!\n")
    input("Presiona Enter para continuar...\n")
    print("-" * 30)
    print("\n¿Cómo te llamas?\n")
    name = input("Ingresa el nombre de tu personaje: \n")
    print("-" * 30)

    while True:
        print("\nSelecciona tu clase:")
        print("1. Guerrero")
        print("2. Mago")
        print("3. Arquero")

        choice = input("\nIngresa el número de tu elección: \n")
        

        if choice == "1":
            return Warrior(name)
        elif choice == "2":
            return Mage(name)
        elif choice == "3":
            return Archer(name)
        else:
            print("\nSelección no válida. Por favor, elige nuevamente.\n")
            input("Presiona Enter para continuar...\n")
            print("-" * 30)


player = create_player()
print("-" * 30)
print("\n")
if player is not None:
    player.display_stats()
print("\n")
input("Presiona Enter para continuar...\n")
print("\n")

print("-" * 30)
print("\nMaravilloso.\n")
input("Presiona Enter para continuar...\n")
print("-" * 30)
print("\nEstás a punto de adentrarte en una misión crucial, valiente aventurero.\n")
input("Presiona Enter para continuar...\n")
print("-" * 30)
print("\nLa diosa Eira te ha elegido como su esperanza.\n")
input("Presiona Enter para continuar...\n")
print("-" * 30)
print("\nEl reino de Eiravir está en peligro, y solo tú puedes enfrentarte a la amenaza que se cierne sobre nosotros.\n")
input("\nPresiona Enter para continuar...\n")
print("-" * 30)
print("\nTu misión es cerrar la brecha que ha sido abierta por Umbra, derrotar a sus sirvientes oscuros y restaurar la paz en Eiravir.\n")
input("Presiona Enter para continuar...\n")
print("-" * 30)
print("\nAdelante.\n")
input("Presiona Enter para continuar...\n")
print("-" * 30)
print("\nY que la bendición de Eira te acompañe en tu viaje.\n")
input("Presiona Enter para comenzar tu aventura...\n")