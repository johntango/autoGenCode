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
def main():
    weight = float(input("Enter the weight of the item (in kg): "))
    cost = calculate_shipping_cost(weight)
    if type(cost) == str:
        print(cost)
    else:
        print(f"The shipping cost is ${cost:.2f}")
if __name__ == "__main__":
    main()
