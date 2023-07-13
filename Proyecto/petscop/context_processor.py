def total_carrito(request):
    total = 0
    carrito = request.session.get("carrito", {})
    if carrito:
        for key, value in carrito.items():
            total += int(value["acumulado"])
    return {"total_carrito": total}
