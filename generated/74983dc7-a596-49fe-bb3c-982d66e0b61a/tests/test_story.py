import pytest

def calculate_shipping_cost(weight, distance):
    if weight <= 0 or distance <= 0:
        raise ValueError("Weight and distance must be positive values.")
    base_cost = 5.0
    cost_per_kg = 2.0
    cost_per_km = 0.5
    return base_cost + (cost_per_kg * weight) + (cost_per_km * distance)

def test_calculate_shipping_cost_valid():
    assert calculate_shipping_cost(10, 100) == 65.0
    assert calculate_shipping_cost(0, 100) == pytest.raises(ValueError)
    assert calculate_shipping_cost(10, 0) == pytest.raises(ValueError)

def test_calculate_shipping_cost_zero_weight():
    with pytest.raises(ValueError):
        calculate_shipping_cost(0, 100)

def test_calculate_shipping_cost_zero_distance():
    with pytest.raises(ValueError):
        calculate_shipping_cost(10, 0)

def test_calculate_shipping_cost_negative_weight():
    with pytest.raises(ValueError):
        calculate_shipping_cost(-5, 100)

def test_calculate_shipping_cost_negative_distance():
    with pytest.raises(ValueError):
        calculate_shipping_cost(10, -50)

def test_calculate_shipping_cost_large_values():
    assert calculate_shipping_cost(1000, 1000) == 2005.0