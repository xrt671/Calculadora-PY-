BANNER = r"""
██   █  ███   ███  █   █ ███ █   █  ███   ████    ████  █   █ 
██ ██ █   █ █   █ █   █  █  ██  █ █   █ █        █   █  █ █  
█ █ █ █████ █   █ █   █  █  █ █ █ █████  ███     ████    █   
█   █ █   █ █  █  █   █  █  █  ██ █   █     █    █       █   
█   █ █   █  ██ █  ███  ███ █   █ █   █ ████     █       █   
"""

BASES = {"1": 10, "2": 2, "3": 8, "4": 16}
NOMBRES = {10: "decimal", 2: "binario", 8: "octal", 16: "hexadecimal"}


def validar_numero(numero, base):
    """Valida que el numero ingresado sea valido para la base indicada."""
    numero = numero.strip()
    try:
        int(numero, base)
        return True
    except ValueError:
        return False


def convertir_a_decimal(numero, base_origen):
    """Convierte un numero desde su base de origen a decimal (entero base 10)."""
    return int(numero, base_origen)


def convertir_desde_decimal(valor_decimal, base_destino):
    """Convierte un valor decimal al string correspondiente en la base destino."""
    if base_destino == 10:
        return str(valor_decimal)
    elif base_destino == 2:
        return bin(valor_decimal)[2:]
    elif base_destino == 8:
        return oct(valor_decimal)[2:]
    elif base_destino == 16:
        return hex(valor_decimal)[2:].upper()


def mostrar_explicacion(numero, base_origen, valor_decimal, base_destino, resultado):
    """Muestra una explicación detallada de la conversión."""
    print("\n" + "~" * 40)
    print("           EXPLICACIÓN DEL PROCESO")
    print("~" * 40)
    
    # Paso 1: A decimal (si no estaba ya en decimal)
    if base_origen != 10:
        print(f"1. Convertimos '{numero}' de {NOMBRES[base_origen]} a decimal (base 10):")
        print(f"   -> Multiplicamos cada dígito por sus potencias correspondientes y sumamos.")
        print(f"   -> Resultado intermedio en decimal: {valor_decimal}")
    else:
        print(1, f"El número ya está en base decimal: {valor_decimal}")

    # Paso 2: De decimal a la base destino (si no es decimal)
    if base_destino != 10:
        print(f"\n2. Convertimos el valor decimal ({valor_decimal}) a {NOMBRES[base_destino]}:")
        if base_destino == 2:
            print("   -> Se divide sucesivamente entre 2 guardando los residuos.")
        elif base_destino == 8:
            print("   -> Se divide sucesivamente entre 8 guardando los residuos.")
        elif base_destino == 16:
            print("   -> Se divide sucesivamente entre 16 (los valores mayores a 9 usan letras A-F).")
        print(f"   -> Resultado final: {resultado}")
    else:
        print(f"\n2. El resultado final en decimal es: {resultado}")
    
    print("~" * 40 + "\n")


def menu_origen():
    print("=" * 40)
    print("    CALCULADORA DE CONVERSION DE BASES")
    print("=" * 40)
    print("Elige la base en la que vas a introducir el numero:")
    print("1. Decimal (base 10)")
    print("2. Binario (base 2)")
    print("3. Octal (base 8)")
    print("4. Hexadecimal (base 16)")
    print("0. Salir")


def menu_destino(base_origen):
    print(f"\nHas elegido {NOMBRES[base_origen]}. Ahora elige a que base quieres convertir:")
    for opcion, base in BASES.items():
        if base != base_origen:
            print(f"{opcion}. Pasar a {NOMBRES[base]}")
    print("0. Volver al menu principal")


def main():
    while True:
        menu_origen()
        opcion = input("Opcion: ").strip()

        if opcion == "0":
            print("Creditos : JMMI")
            break

        if opcion not in BASES:
            print("Opcion no valida, intentalo de nuevo.\n")
            continue

        base_origen = BASES[opcion]
        numero = input(f"Introduce el numero en {NOMBRES[base_origen]}: ").strip()

        if not validar_numero(numero, base_origen):
            print(f"Error: '{numero}' no es un numero valido en base {base_origen}.\n")
            continue

        valor_decimal = convertir_a_decimal(numero, base_origen)

        menu_destino(base_origen)
        opcion_destino = input("Opcion: ").strip()

        if opcion_destino == "0":
            continue

        if opcion_destino not in BASES or BASES[opcion_destino] == base_origen:
            print("Opcion no valida.\n")
            continue

        base_destino = BASES[opcion_destino]
        resultado = convertir_desde_decimal(valor_decimal, base_destino)

        print(f"\n{numero} ({NOMBRES[base_origen]}) = {resultado} ({NOMBRES[base_destino]})\n")

        # Nuevas opciones después de mostrar el resultado
        while True:
            print("¿Qué deseas hacer ahora?")
            print("1. Ver explicación")
            print("2. Finalizar / Nueva conversión")
            sub_opcion = input("Opcion: ").strip()

            if sub_opcion == "1":
                mostrar_explicacion(numero, base_origen, valor_decimal, base_destino, resultado)
            elif sub_opcion == "2":
                print("")
                break
            else:
                print("Opción no válida, intenta de nuevo.\n")


if __name__ == "__main__":
    print(BANNER)
    main()
