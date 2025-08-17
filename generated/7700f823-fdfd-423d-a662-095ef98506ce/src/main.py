def calculate_shipping_cost(weight):
    if weight <= 0:
        return "Invalid weight"
    elif weight <= 5:
        return 5.0  # Flat rate for <= 5kg
    elif weight <= 20:
        return 10.0  # Flat rate for 6-20kg
    else:
        return 15.0 + (weight - 20) * 0.5  # Additional cost for each kg over 20kg
weight = float(input("Enter the weight of the item in kg: "))
cost = calculate_shipping_cost(weight)
print(f"The shipping cost is: ${cost}")
