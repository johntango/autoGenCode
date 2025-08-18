def calculate_shipping_cost(weight):
    if weight <= 5:
        return 5.0  # flat rate for packages up to 5kg
    elif weight <= 10:
        return 10.0  # flat rate for packages between 5kg and 10kg
    else:
        return 10.0 + (weight - 10) * 1.5  # additional cost for weight over 10kg

weight_of_package = 12  # example weight
cost = calculate_shipping_cost(weight_of_package)
print(f"The shipping cost for a package weighing {weight_of_package}kg is ${cost:.2f}")
