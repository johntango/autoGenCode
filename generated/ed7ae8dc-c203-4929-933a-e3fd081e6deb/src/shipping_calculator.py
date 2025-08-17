def calculate_shipping_cost(weight):
    base_cost = 5.00
    if weight <= 0:
        raise ValueError('Weight must be positive.')
    elif weight <= 2:
        cost = base_cost + (weight * 1.50)
    elif weight <= 5:
        cost = base_cost + (weight * 2.50)
    else:
        cost = base_cost + (weight * 3.50)
    return cost

def main():
    try:
        weight = float(input('Enter the weight of the item in kg: '))
        cost = calculate_shipping_cost(weight)
        print(f'Total shipping cost: ${cost:.2f}')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
