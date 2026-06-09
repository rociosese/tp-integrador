def calcular_total(compras):
  total = 0

  for compra in compras:
    total += compra["cantidad"] * compra["precio"]

  return total


def producto_mas_vendido(compras):
  cantidades = {}

  for compra in compras:
    producto = compra["producto"]

    if producto not in cantidades:
      cantidades[producto] = 0

    cantidades[producto] += compra["cantidad"]

  return max(cantidades, key=cantidades.get)
  
    
