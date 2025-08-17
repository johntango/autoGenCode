def calculate_shipping_cost(weight):
    if weight <= 5:
        return 5  # Base price for items up to 5kg
    elif 5 < weight <= 20:
        return 10  # Price for items between 5kg and 20kg
    else:
        return 20  # Price for items above 20kg

# Example usage
weight = float(input("Enter the weight of the item in kg: "))
cost = calculate_shipping_cost(weight)
print(f"The shipping cost is: ${cost}")
