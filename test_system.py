import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Caso 1: Flujo completo del TRY (Respuesta 200)
def test_sistema_calcular_precio_try(client):
    payload = {"precio": 500, "descuento": 20}
    response = client.post('/calcular-precio', json=payload)
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["precio_final"] == 400.0

# Caso 2: Flujo completo del EXCEPT (Respuesta 400 por datos erróneos)
def test_sistema_calcular_precio_exception(client):
    payload = {"precio": 500, "descuento": -10}  # Inválido
    response = client.post('/calcular-precio', json=payload)
    
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert "El descuento debe estar entre 0 y 100" in data["error"]

# Caso extra para peso de envío (TRY y EXCEPT)
def test_sistema_calcular_peso_try(client):
    payload = {"peso_unitario": 2.0, "cantidad": 3, "peso_empaque": 0.5}
    response = client.post('/calcular-peso', json=payload)
    
    assert response.status_code == 200
    assert response.get_json()["peso_total"] == 6.5

def test_sistema_calcular_peso_exception(client):
    payload = {"peso_unitario": -2.0, "cantidad": 3}
    response = client.post('/calcular-peso', json=payload)
    
    assert response.status_code == 400
    assert "El peso unitario y la cantidad deben ser mayores a 0" in response.get_json()["error"]