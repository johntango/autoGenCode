def calculate_shipping_cost(weight):
    if weight <= 5:
        return 5.0
    elif weight <= 10:
        return 10.0
    elif weight <= 20:
        return 15.0
    else:
        return 25.0

weight = float(input("Enter the weight of the package in kg: "))
cost = calculate_shipping_cost(weight)
print(f"The shipping cost is: ${cost:.2f}")
