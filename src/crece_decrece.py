def contar_crecientes_decrecientes(x, y):
    # Borre el comando pass y escriba su código
    # No olvide que debe retonar 3 datos
    pass


##########################################################
##### NO MODIFIQUE de aquí en adelante
##########################################################
def main():
    # Prueba con x = 3
    x = int(input("Ingrese un valor entero positivo >> "))
    y = int(input("Ingrese un valor entero positivo >> "))
    crecientes, decreientes, total = contar_crecientes_decrecientes(x, y)
    if total == -1:
        print("Los valores ingresados deben ser positivos.")
    else:
        print(f"Crecientes: {crecientes}\nDecrecientes: {decreientes}\nTotal: {total}")


if __name__ == "__main__":
    main()
