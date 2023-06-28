def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                # Verificar si la clave "acumulado" existe en el elemento del carrito
                if "acumulado" in value:
                    total += int(value["acumulado"])
    return {"total_carrito": total}