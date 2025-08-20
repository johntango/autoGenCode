def calculate_shipping_cost(weight, story):
    base_cost = 5.0
    cost_per_kg = 2.0
    story_multiplier = {'fragile': 1.5, 'express': 2.0, 'standard': 1.0}
    weight_cost = base_cost + (weight * cost_per_kg)
    multiplier = story_multiplier.get(story, 1.0)
    return weight_cost * multiplier
weight = float(input("Enter the weight of the package in kg: "))
story = input("Enter the story (fragile, express, standard): ")
cost = calculate_shipping_cost(weight, story)
print(f"Total shipping cost: ${cost:.2f}")
