import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.compras import calcular_total, producto_mas_vendido

def test_calcular_total():
  compras = [
    {"producto" : "arroz", "cantidad": 2, "precio": 1000},
    {"producto" : "fideos", "cantidad": 3, "precio": 500}
  ]

  assert calcular_total(compras) == 3500

def test_producto_mas_vendido():
  compras = [
    {"producto" : "arroz", "cantidad": 2, "precio": 1000},
    {"producto" : "fideos", "cantidad": 5, "precio": 500}
  ]

  assert producto_mas_vendido(compras) == "fideos"

def test_total_vacio():
  compras = []

  assert calcular_total(compras) == 0

def test_un_solo_producto():
  compras = [
    {"producto" : "leche", "cantidad": 1, "precio": 1000}
  ]

  assert calcular_total(compras) == 9999

def test_producto_mas_vendido_unico():
  compras = [
    {"producto" : "agua", "cantidad": 10, "precio": 100}
  ]

  assert producto_mas_vendido(compras) == "agua"


