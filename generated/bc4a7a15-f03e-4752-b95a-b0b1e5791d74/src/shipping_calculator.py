def calculate_shipping_cost(weight):
    if weight <= 5:
        return 5.0  # Flat rate for packages 5kg or less
    else:
        return 5.0 + (weight - 5) * 1.5  # Additional rate for every kg over 5kg

# Example usage:
package_weight = 10
cost = calculate_shipping_cost(package_weight)
print(f"The shipping cost for a package weighing {package_weight} kg is: ${cost:.2f}")
