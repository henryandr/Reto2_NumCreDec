import pytest
from src.crece_decrece import contar_crecientes_decrecientes


# Prueba con valores válidos para x e y
@pytest.mark.parametrize(
    "input_x, input_y, expected_cre, expected_dec, expected_tot",
    [
        (1, 5, 5, 0, 5),
        (200, 2000, 285, 212, 497),
        (1000, 10000, 495, 706, 1201),
        (1, 100000, 2001, 2953, 4954),
        (50000, 1000000, 3129, 6867, 9996),
    ],
)
def test_valores_validos(input_x, input_y, expected_cre, expected_dec, expected_tot):
    cre, dec, tot = contar_crecientes_decrecientes(input_x, input_y)
    assert cre == expected_cre
    assert dec == expected_dec
    assert tot == expected_tot


# Prueba con x y y iguales
def test_x_y_iguales():
    resultado = contar_crecientes_decrecientes(3, 3)
    assert resultado == (1, 0, 1)


# Prueba con x mayor que y
@pytest.mark.parametrize(
    "input_x, input_y, expected_cre, expected_dec, expected_tot",
    [
        (90000, 100, 1946, 2194, 4140),
        (2500, 300, 334, 215, 549),
        (1000000, 400000, 462, 4916, 5378),
    ],
)
def test_x_mayor_que_y(input_x, input_y, expected_cre, expected_dec, expected_tot):
    cre, dec, tot = contar_crecientes_decrecientes(input_x, input_y)
    assert cre == expected_cre
    assert dec == expected_dec
    assert tot == expected_tot


# Prueba con x y y negativos
def test_valores_negativos():
    resultado = contar_crecientes_decrecientes(-2, -7)
    assert resultado == -1


# Prueba con x negativo e y positivo
def test_x_negativo_y_positivo():
    resultado = contar_crecientes_decrecientes(-3, 4)
    assert resultado == -1


# Prueba con x negativo e y positivo
def test_x_positivo_y_negativo():
    resultado = contar_crecientes_decrecientes(100, -200)
    assert resultado == -1


# Prueba para verificar el número de argumentos
def test_numero_argumentos_correcto():
    with pytest.raises(TypeError):
        contar_crecientes_decrecientes(1)  # Llamamos a la función con un solo argumento
        contar_crecientes_decrecientes()
        contar_crecientes_decrecientes(3, 56, 67)


if __name__ == "__main__":
    pytest.main()
