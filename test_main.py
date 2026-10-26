import pytest
import main

# Caso 1: Resultado entra al TRY (Exitoso)
def test_main_exitoso_try(monkeypatch, capsys):
    entradas = iter(["200", "10"])  # precio=200, descuento=10%
    monkeypatch.setattr('builtins.input', lambda _: next(entradas))
    
    resultado = main.main()
    salida = capsys.readouterr().out
    
    assert resultado == 180.0
    assert "Precio final: 180.00" in salida

# Caso 2: Resultado entra al EXCEPT (Manejo de error)
def test_main_error_exception(monkeypatch, capsys):
    entradas = iter(["200", "150"])  # Descuento inválido (> 100)
    monkeypatch.setattr('builtins.input', lambda _: next(entradas))
    
    resultado = main.main()
    salida = capsys.readouterr().out
    
    assert resultado is None
    assert "Error: El descuento debe estar entre 0 y 100" in salida