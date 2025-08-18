def calculate_shipping_cost(weight):
    if weight <= 0:
        raise ValueError("Weight must be positive")
    elif weight <= 5:
        cost = 5.0 + (weight * 1.0)
    elif weight <= 20:
        cost = 10.0 + (weight * 0.75)
    else:
        cost = 15.0 + (weight * 0.5)
    return cost

# Example usage
weight = 10  # in kilograms
shipping_cost = calculate_shipping_cost(weight)
print(f"Shipping cost for {weight} kg is ${shipping_cost}")
