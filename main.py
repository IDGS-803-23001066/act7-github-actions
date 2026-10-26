from app import calcular_precio, calcular_peso_envio

def main():
    try:
        precio = float(input("Ingrese el precio del producto: "))
        descuento = float(input("Ingrese el porcentaje de descuento: "))
        
        precio_final = calcular_precio(precio, descuento)
        print(f"Precio final: {precio_final:.2f}")
        return precio_final
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    main()