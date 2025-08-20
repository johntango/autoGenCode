def calculate_shipping_cost(weight):
    if weight <= 0:
        return "Invalid weight"
    elif weight <= 5:
        return 5.00
    elif weight <= 10:
        return 10.00
    elif weight <= 20:
        return 15.00
    else:
        return 20.00
weight = float(input("Enter the package weight in kg: "))
cost = calculate_shipping_cost(weight)
print(f"The shipping cost is: ${cost}")
