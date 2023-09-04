names = ['Bruce', 'Clark', 'Peter']
heroes = ['Batman', 'Superman', 'Spiderman']
# print(list(zip(names, heroes)))

my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Clark'}
# for name, hero in zip(names,heroes):
#     my_dict[name] = hero
print(my_dict)
