def calculate_shipping_cost(weight):
    if weight <= 5:
        return 5.0  # Base cost for weight <= 5 units
    elif weight <= 10:
        return 10.0  # Cost for weight between 5 and 10 units
    elif weight <= 20:
        return 20.0  # Cost for weight between 10 and 20 units
    else:
        return 50.0  # Cost for weight over 20 units

# Example Usage:
item_weight = 7
cost = calculate_shipping_cost(item_weight)
print(f"Shipping cost for {item_weight} units: ${cost}")
