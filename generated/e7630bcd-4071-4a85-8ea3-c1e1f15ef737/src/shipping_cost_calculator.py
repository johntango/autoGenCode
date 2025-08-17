def calculate_shipping_cost(weight):
    if weight <= 5:
        return 5.00  # Flat rate for weights <= 5kg
    else:
        return 5.00 + (weight - 5) * 1.50  # Additional cost for each kg over 5kg


# Get input from the user
item_weight = float(input("Enter the weight of the item in kg: "))

# Calculate the shipping cost
cost = calculate_shipping_cost(item_weight)

# Display the result
print(f"The shipping cost is: ${cost:.2f}")
