def calculate_shipping_cost(weight):
    if weight <= 0:
        return "Invalid weight"
    elif weight <= 5:
        return 5.00
    elif weight <= 20:
        return 10.00
    else:
        return 20.00

# Example Usage:
package_weight = 10  # Weight in kg
cost = calculate_shipping_cost(package_weight)
print(f"The shipping cost is: ${cost:.2f}")
