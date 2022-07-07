  # Actividad relacionada con la lección 2:
  # test utilizabdo pytest
  # 
  # # importancion de las libreria
import pytest
import matematicas

def test_factorial():
    num = 5
    resultado = 120
    assert resultado == matematicas.factorial(num)


def test_cuadrada():
    num = 9
    resultado = 3
    assert resultado == matematicas.cuadrada(num)


def test_hipo():
    a = 2
    b = 3
    resultado = 13
    assert resultado == matematicas.hipo(a,b)
    

def test_area():
    r = 3
    resultado = 28.274328
    assert resultado == matematicas.area(r)


def test_rectangulo():
    a = 5
    l = 4
    resultado = 20
    assert resultado == matematicas.rectangulo(a,l)
