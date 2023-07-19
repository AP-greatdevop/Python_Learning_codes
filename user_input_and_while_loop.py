# Movie ticket

'''
age = int(input("Enter your age:"))

while age > 2:
    if  age >= 3 and age <= 12:
        ticket = 10
    if age >= 12:
        ticket = 15
    else:
        ticket = 0
    break

print(f"Your ticket fare is {ticket} dollar.")
'''

# Infinity
'''
x = 1
while x > 0:
    x += 1

    print(x)

'''

# Confirmed user.py
'''
# Start with the users that need to be verified,
# and an empty list to hold confirmed users 

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more confirmed users.
# Move each verified user into the list of confirmed user.

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)

# Display all confirmed users.
print("\nThe following users have been confirmed:") 
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print(confirmed_users)
'''

# Removing all instances of specific values from a list

'''
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
'''

# Filling a dictionary with user input
'''
responses = {}

# Set a flag to indicate that polling is active 
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday")
    
    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person to respond ? (yes/no)")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Result---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}. ")

'''

# Deli
'''
sandwich_orders = ['egg', 'seafood', 'roast beef', 'grilled', 'ham']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Making sandwich: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

print(finished_sandwiches)
'''
# No Pastrami
'''

print("The deli has run out of pastrami.")
sandwich_orders = ['egg', 'pastrami', 'seafood', 'pastrami', 'roast beef', 'pastrami', 'grilled', 'pastrami', 'ham']

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
'''

# Dream Vacation
'''
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("If you could visit one place in the world, where would you go?")

    responses[name] = response

    repeat = input("Would you like to let another person respond ? (yes/no)")
    if repeat == 'no':
        polling_active = False

for name, response in responses.items():
    print(f"{name} would like to go {response}.")

'''