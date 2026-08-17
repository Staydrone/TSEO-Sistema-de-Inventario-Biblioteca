# ---------------------------------
# Sistema de Inventario Biblioteca
# ---------------------------------

# Función para validar la categoría del libro
def validar_categoria():
    categorias_validas = ["Ciencia", "Literatura", "Tecnología", "Historia"]

    while True:
        categoria = input(
            "Ingrese la categoría (Ciencia, Literatura, Tecnología, Historia): "
        ).strip().capitalize()

        if categoria in categorias_validas:
            return categoria
        else:
            print("❌ Categoría inválida. Intente nuevamente.")


# Función para validar el código según la categoría
def validar_codigo(categoria):
    sufijos = {
        "Ciencia": "94",
        "Tecnología": "86",
        "Literatura": "37",
        "Historia": "21"
    }

    while True:
        codigo = input("Ingrese el código del libro: ").strip()

        if not codigo.isdigit():
            print("❌ El código debe ser numérico.")
            continue

        if codigo.endswith(sufijos[categoria]):
            return codigo
        else:
            print(f"❌ Error: el código no corresponde a la categoría {categoria}.")


# Función que retorna el precio según la categoría
def obtener_precio(categoria):
    precios = {
        "Ciencia": 80000,
        "Literatura": 50000,
        "Tecnología": 100000,
        "Historia": 60000
    }
    return precios[categoria]


# Procedimiento principal
def inventario_biblioteca():
    nombres = []
    codigos = []
    categorias = []
    cantidades = []

    total_libros = 0
    valor_total = 0

    contadores = {
        "Ciencia": 0,
        "Literatura": 0,
        "Tecnología": 0,
        "Historia": 0
    }

    N = int(input("Ingrese el número de libros a registrar: "))

    for i in range(N):
        print(f"\n📘 Libro {i + 1}")

        nombre = input("Ingrese el nombre del libro: ")

        categoria = validar_categoria()

        codigo = validar_codigo(categoria)

        while True:
            cantidad = int(input("Ingrese la cantidad de unidades: "))
            if cantidad > 0:
                break
            else:
                print("❌ La cantidad debe ser mayor que cero.")

        nombres.append(nombre)
        categorias.append(categoria)
        codigos.append(codigo)
        cantidades.append(cantidad)

        precio = obtener_precio(categoria)

        total_libros += cantidad
        valor_total += precio * cantidad
        contadores[categoria] += cantidad

    valor_promedio = valor_total / total_libros if total_libros > 0 else 0

    # Resultados
    print("\n--- RESULTADOS DEL INVENTARIO ---")
    print("Total de libros en inventario:", total_libros)
    print("Valor total del inventario: $", valor_total)
    print("Valor promedio por libro: $", round(valor_promedio, 2))

    print("\nCantidad de libros por categoría:")
    for categoria, cantidad in contadores.items():
        print(f"{categoria}: {cantidad}")

    print("\n--- LIBROS REGISTRADOS ---")
    for i in range(N):
        print(
            f"Código: {codigos[i]} | "
            f"Nombre: {nombres[i]} | "
            f"Categoría: {categorias[i]} | "
            f"Cantidad: {cantidades[i]}"
        )


# Ejecución del programa
inventario_biblioteca()

