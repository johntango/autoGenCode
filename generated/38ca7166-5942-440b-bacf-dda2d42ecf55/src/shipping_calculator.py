def calculate_shipping_cost(weight):
    if weight <= 1:
        return 5.0  # Flat rate for items 1 kg or less
    elif weight <= 5:
        return 10.0  # Flat rate for items between 1 kg and 5 kg
    elif weight <= 10:
        return 20.0  # Flat rate for items between 5 kg and 10 kg
    else:
        return 20.0 + (weight - 10) * 1.5  # Additional cost for items over 10 kg
def main():
    weight = float(input("Enter the weight of the item (in kg): "))
    cost = calculate_shipping_cost(weight)
    print(f"The shipping cost is: ${cost:.2f}")

if __name__ == "__main__":
    main()
