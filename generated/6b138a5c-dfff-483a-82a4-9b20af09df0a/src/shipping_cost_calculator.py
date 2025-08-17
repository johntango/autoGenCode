def calculate_shipping_cost(weight):
    if weight <= 0:
        return "Invalid weight"
    elif weight <= 5:
        return weight * 5
    else:
        return 25 + (weight - 5) * 3
def calculate_discounted_shipping(weight):
    cost = calculate_shipping_cost(weight)
    return cost * 0.9 if isinstance(cost, (int, float)) else cost
