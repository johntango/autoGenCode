def calculate_shipping_cost(weight):
    if weight <= 0:
        raise ValueError("Weight must be positive")
    elif weight <= 1:
        return 5.0  # Flat rate for weight <= 1kg
    elif weight <= 5:
        return 10.0 + (weight - 1) * 1.5  # Additional rate for weight between 1kg and 5kg
    else:
        return 16.0 + (weight - 5) * 2.0  # Higher rate for weight above 5kg

# Example usage
weight = 3.5
cost = calculate_shipping_cost(weight)
print(f"The shipping cost for {weight} kg is ${cost:.2f}")
