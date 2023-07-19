# alien_0 = {'colour': 'green', 'points': 5}

# print(alien_0['colour'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# alien_0 = {}
# alien_0['colour'] = 'green'
# alien_0['points'] = 5

# print(alien_0)



# alien_0 = {'colour': 'green'}
# print(f"The alien is {alien_0['colour']}")

# alien_0['colour'] = 'yellow'
# print(f"The alien is {alien_0['colour']}")


# alien_0 = {'colour': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

# alien_0 = {'colour': 'green', 'speed': 'slow'}
# # print(alien_0['points'])

# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)



# alien_0 = {'colour': 'green', 'points': 5}
# alien_1 = {'colour': 'yellow', 'points': 10}
# alien_2 = {'colur': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# # Show how many aliens have been created.
# print(f"Total number of aliens: {len(aliens)}")