inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

#Add a key to inventory called 'pocket'.
inventory["pocket"] = ['seashell', 'strange berry', 'lint']
print('\nAfter add key')
for i in inventory:
    print(i,inventory[i])

#Del 'dagger' from 'backpack'
del inventory['backpack'][1]

print("\nAfter remove 'dagger' from 'backpack'\n")
for i in inventory:
    print(i,inventory[i])

#Add 50 to the number stored under the 'gold' key.
inventory['gold'] = 50
print("\nAfter add 50 to the number stored under the 'gold' key\n")
for i in inventory:
    print(i,inventory[i])

