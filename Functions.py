# Defining a function

'''
def greet_user():
    """Display a simple greeting"""
    print("Hello!") 

greet_user()
'''

# Passing information to a function
'''
def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!") 

greet_user('jessa')
'''
# Message
'''
def display_message():
    print("What are you learning about this chapter.")

display_message()
'''

# Favourite Book
'''
def favourite_book(title):
    print(f"One of my favourite book is {title.title()}")

favourite_book('python crash course')
'''
# Positional Arguments
'''
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.") 
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
'''

# Multiple Function Calls
'''
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.") 
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
'''
# Keyword Arguments
'''
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.") 
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')           
describe_pet(pet_name='harry', animal_type='hamster')         
'''

# Default Values
'''
def describe_pet(pet_name, animal_type= 'dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.") 
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet('willie')
'''

# T-Shirt
'''
def make_shirt(size, text_message):
    print(f"Size of the shirt is {size} and the message that should be printed on the shirt is '{text_message}'.")

make_shirt("L", "Flower Nahi Fire Hai Main ")
'''

# large Shirts
'''
def make_shirt(text_message, size = 'L'):
    print(f"Size of the shirt is {size} and the message that should be printed on the shirt is '{text_message}'.")

make_shirt("I Love Python")
'''
'''
def make_shirt(size, text_message = "I Love Python"):
    print(f"Size of the shirt is {size} and the message that should be printed on the shirt is '{text_message}'.")

make_shirt(size= "Large")
make_shirt(size= "Medium")
'''
# Cities
'''
def describe_city(city, country):
    print(f"{city.title()} is in {country.title()}.")

describe_city("karbi anglong", "india")


def describe_city(city, country = "india"):
    print(f"{city.title()} is in {country.title()}.")

describe_city("karbi anglong")
'''

# formatted_name.py
'''
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimmy', 'hendrix')
print(musician)
'''

# Making an additional argument
'''
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formated."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
'''
'''
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimmi', 'hendrix')
print(musician)

musicianc = get_formatted_name('john', 'hooker', 'lee')
print(musician)
'''
#Album
'''
def make_album(artist_name, album_name, song_numbers=None):
    song = {'artist': artist_name, 'album': album_name, 'songs': song_numbers}
    
    return song

singer = make_album("arijitsingh", "Ashique2", song_numbers=4)
print(singer)
'''
#User Album
'''
def make_album(artist_name, album_name, song_numbers=None):
    song = {'artist': artist_name, 'album': album_name, 'songs': song_numbers}
    return song

while True:
    print("\nPlease tell me your artist name, album name and song numbers:")
    print("(enter 'q' at any time to quit)")

    artist_n = input("Artist name:")
    if artist_n == 'q':
        break

    album_n = input("Album name:")
    if album_n == 'q':
        break

    song_n = input("Song numbers:")
    if song_n == 'q':
        break

singer = make_album(artist_n, album_n, song_n)
print(f"\nYour song location is {singer}")
'''
# Passing a list
def greet_users(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)