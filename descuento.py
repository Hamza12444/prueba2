def calcular_descuento(importe: float) -> tuple[float, float, float]:
    """Calcula el porcentaje de descuento, la cantidad ahorrada y el total a pagar.

    Args:
        importe (float): Importe inicial de la compra.

    Returns:
        tuple: Contiene (porcentaje_aplicado, cantidad_descuento, total_a_pagar).
    """
    if importe >= 300.0:
        porcentaje = 15.0
    elif importe >= 100.0:
        porcentaje = 10.0
    else:
        porcentaje = 0.0

    descuento = importe * (porcentaje / 100.0)
    total_pagar = importe - descuento

    return porcentaje, descuento, total_pagar


def main() -> None:
    """Función principal que gestiona la entrada de datos y muestra los resultados."""
    print("=== GESTIÓN DE DESCUENTOS DE LA TIENDA ===")

    try:
        entrada = input("Introduce el importe total de la compra (€): ")
        importe = float(entrada)

        if importe < 0:
            print("Error: El importe de la compra no puede ser negativo.")
            return

        porcentaje, descuento, total = calcular_descuento(importe)

        print("\n--- RESUMEN DE LA COMPRA ---")
        print(f"Importe inicial:    {importe:10.2f} €")
        print(f"Descuento aplicado: {porcentaje:10.0f} %")
        print(f"Cantidad ahorrada:  {descuento:10.2f} €")
        print(f"Total a pagar:      {total:10.2f} €")

    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce un valor numérico.")


if __name__ == "__main__":
    main()