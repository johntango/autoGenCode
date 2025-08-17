def calculate_shipping_cost(weight):
    if weight <= 0:
        raise ValueError("Weight must be a positive number.")
    
    if weight <= 5:
        return 5  # Flat rate for items up to 5 kg
    elif weight <= 10:
        return 10  # Flat rate for items between 5 and 10 kg
    elif weight <= 20:
        return 20  # Flat rate for items between 10 and 20 kg
    else:
        return 50  # Flat rate for items over 20 kg
    
# Example usage
weight = 8
cost = calculate_shipping_cost(weight)
print(f"The shipping cost for an item weighing {weight} kg is ${cost}.")
