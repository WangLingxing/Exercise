stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def display_inventory(inventory):
    print('inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

# 新增的项目
def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(inv, dragonLoot)
display_inventory(inv)
