def calculate_shipping_cost(weight):
    if weight <= 0:
        return 0
    elif weight <= 5:
        return 5
    elif weight <= 20:
        return 10
    else:
        return 20
def main():
    weight = float(input("Enter the package weight in kg: "))
    cost = calculate_shipping_cost(weight)
    print(f"The shipping cost is: ${cost}")
if __name__ == "__main__":
    main()
