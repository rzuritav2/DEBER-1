def main():
    print("DIVISORES")
    numero = int(input("Escriba un número entero mayor que cero: "))

    if numero <= 0:
        print("¡Le he pedido un número entero mayor que cero!")
    else:
        print(f"el numero mayor es:",numero )
        for i in range(1, numero + 1):
            if numero % i == 0:
                print(i, end=" ")


if __name__ == "__main__":
    main()