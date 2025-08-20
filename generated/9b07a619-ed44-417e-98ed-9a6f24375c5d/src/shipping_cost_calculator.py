def calculate_shipping_cost(weight):
    if weight <= 5:
        return 5.00
    elif weight <= 10:
        return 10.00
    elif weight <= 20:
        return 15.00
    else:
        return 25.00

# Get user input
def main():
    try:
        weight = float(input("Enter the package weight (in kg): "))
        cost = calculate_shipping_cost(weight)
        print(f"The shipping cost is: ${cost:.2f}")
    except ValueError:
        print("Please enter a valid number for the weight.")

main()
