# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings' : ['mushrooms', 'extra cheese']
}

# Summerize the order.
print(f"You ordered a {pizza['crust']}-crust pizza"
    "\twith the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)