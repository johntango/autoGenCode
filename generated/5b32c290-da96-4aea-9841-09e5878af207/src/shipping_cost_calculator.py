def calculate_shipping_cost(weight):
    if weight <= 5:
        return 5.00
    elif weight <= 20:
        return 10.00
    else:
        return 20.00

# Example usage:
package_weight = 10  # weight in kg
cost = calculate_shipping_cost(package_weight)
print(f"The shipping cost for a package weighing {package_weight} kg is ${cost:.2f}.")
