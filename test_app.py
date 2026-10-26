import pytest
from app import calcular_precio, calcular_peso_envio

def test_calcular_precio():
    assert calcular_precio(100, 10) == 90

def test_calcular_sin_descuento():
    assert calcular_precio(500, 0) == 500

def test_descuento_invalido():
    with pytest.raises(ValueError):
        calcular_precio(100, 110)

def test_calcular_peso_envio():
    assert calcular_peso_envio(2.0, 3) == pytest.approx(6.5)

def test_calcular_peso_invalido():
    with pytest.raises(ValueError):
        calcular_peso_envio(-1, 2)