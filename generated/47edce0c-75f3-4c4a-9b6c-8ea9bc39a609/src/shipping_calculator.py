def calculate_shipping_cost(weight):
    if weight <= 5:
        return 5  # Flat rate for 5kg or less
    elif weight <= 20:
        return 10  # Flat rate for 6kg to 20kg
    else:
        return 15 + (weight - 20) * 0.5  # Higher rate for over 20kg

weight = float(input("Enter the weight of the package in kg: "))
cost = calculate_shipping_cost(weight)
print(f"The shipping cost is: ${cost}")
