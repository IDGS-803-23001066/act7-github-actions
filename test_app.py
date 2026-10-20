import pytest
from app import app, calcular_precio, calcular_peso_envio

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Pruebas unitarias
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

# Pruebas de endpoints Flask
def test_endpoint_calcular_precio(client):
    response = client.post('/calcular-precio', json={"precio": 200, "descuento": 20})
    assert response.status_code == 200
    assert response.get_json()["precio_final"] == 160

def test_endpoint_calcular_peso(client):
    response = client.post('/calcular-peso', json={"peso_unitario": 1.5, "cantidad": 2})
    assert response.status_code == 200
    assert response.get_json()["peso_total"] == 3.5