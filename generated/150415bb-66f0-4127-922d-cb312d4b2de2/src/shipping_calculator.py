def calculate_shipping_cost(weight):
    base_cost = 5.00
    additional_cost_per_kg = 1.50
    if weight <= 1:
        return base_cost
    else:
        return base_cost + (weight - 1) * additional_cost_per_kg

weight = float(input("Enter the package weight in kg: "))
cost = calculate_shipping_cost(weight)
print(f"The shipping cost is: ${cost:.2f}")
