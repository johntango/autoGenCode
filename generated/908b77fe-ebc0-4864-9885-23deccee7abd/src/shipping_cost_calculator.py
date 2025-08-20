def calculate_shipping_cost(weight):
    if weight <= 1:
        cost = 5.00  # Flat rate for packages up to 1 kg
    elif weight <= 5:
        cost = 10.00  # Flat rate for packages between 1 kg and 5 kg
    elif weight <= 10:
        cost = 20.00  # Flat rate for packages between 5 kg and 10 kg
    else:
        cost = 50.00  # Flat rate for packages over 10 kg
    return cost
 
# Example usage
package_weight = 7
shipping_cost = calculate_shipping_cost(package_weight)
print(f"The shipping cost for a package weighing {package_weight} kg is ${shipping_cost:.2f}")
