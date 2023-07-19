# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# peoples = ['francis', 'george', 'sarah', 'phil']

# for people in peoples:
#     print(people.title())

#     if people in favourite_languages.keys():
#         print(f"\t{people.title()}, thanks for having a poll.")
#     else:
#         print(f"\t{people.title()}, please take a poll.")

def build_person(first_name, last_name, age=None):
 """Return a dictionary of information about a person."""
 person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)





# for name in favourite_languages.keys():
#     print(name.title())

#     if name in people:
#         print(f"\t{name.title()}, thanks for having a poll.")
#     else:
#         print(f"\t{name.title()}, please take a poll.")




# print("The following languages have been mentioned:")
# for language in favourite_languages.values():
#     print(language.title())


# language = favourite_languages['sarah'].title()
# print(f"Sarah's favourite language is {language}.")

# for people, language in favourite_languages.items():
# #     print(f"\npeople: {people}")
# #     print(f"langusge: {language}")
#     print(f"{people.title()}'s favourite lanuguage is {language.title()}.")

# for people in favourite_languages.keys():
# #     print(people.title())

# for people in favourite_languages:
#     print(people.title())


# friends = ['phil', 'sarah']
# for people in favourite_languages.keys():
#     print(people.title())

#     if people in friends:
#         language = favourite_languages[people].title()
#         print(f"\t{people.title()}, I see you love {language}!")


# if 'erin' not in favourite_languages.keys():
#     print("Erin, please take our poll!")

# for people in sorted(favourite_languages.keys()):
#     print(f"{people.title()}, thank you for taking the poll.")

'''

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

'''






        







