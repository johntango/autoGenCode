import pytest

def calculate_shipping_cost(weight, distance):
    if weight <= 0 or distance < 0:
        raise ValueError("Weight must be positive and distance cannot be negative.")
    base_cost = 5.0
    weight_cost = weight * 0.5
    distance_cost = distance * 0.1
    return base_cost + weight_cost + distance_cost

def test_calculate_shipping_cost_valid():
    assert calculate_shipping_cost(10, 100) == 15.0
    assert calculate_shipping_cost(5, 50) == 10.0
    assert calculate_shipping_cost(0, 0) == 5.0

def test_calculate_shipping_cost_zero_weight():
    with pytest.raises(ValueError):
        calculate_shipping_cost(0, 100)

def test_calculate_shipping_cost_negative_weight():
    with pytest.raises(ValueError):
        calculate_shipping_cost(-1, 100)

def test_calculate_shipping_cost_negative_distance():
    with pytest.raises(ValueError):
        calculate_shipping_cost(10, -1)

def test_calculate_shipping_cost_large_values():
    assert calculate_shipping_cost(1000, 1000) == 1055.0