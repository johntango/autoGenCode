def calculate_shipping_cost(weight):
    if weight <= 0:
        raise ValueError('Weight must be positive')
    elif weight <= 5:
        return weight * 1.5
    elif weight <= 20:
        return weight * 2.0
    else:
        return weight * 3.0
 
try:
    weight = float(input('Enter the package weight in kg: '))
    cost = calculate_shipping_cost(weight)
    print(f'The shipping cost is: ${cost:.2f}')
except ValueError as ve:
    print(ve)
