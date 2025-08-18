def calculate_shipping_cost(weight):
    if weight <= 0:
        return "Invalid weight"
    elif weight <= 5:
        return weight * 1.5
    elif weight <= 20:
        return 5 * 1.5 + (weight - 5) * 3
    else:
        return 5 * 1.5 + 15 * 3 + (weight - 20) * 4

# Example Usage
weight_of_package = 10
cost = calculate_shipping_cost(weight_of_package)
print(f"The shipping cost is: ${cost}")
