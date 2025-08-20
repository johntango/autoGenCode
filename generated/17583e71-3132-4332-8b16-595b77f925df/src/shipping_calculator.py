def calculate_shipping_cost(weight):
    if weight <= 5:
        cost = weight * 1.5
    elif weight <= 20:
        cost = weight * 1.2
    else:
        cost = weight * 1.0
    return cost

weight = float(input("Enter the package weight in kg: "))
cost = calculate_shipping_cost(weight)
print(f"The shipping cost for a {weight}kg package is ${cost:.2f}.")
