"""Functions to keep track and alter inventory."""


def loop(inventory, items, flag: bool):
    for item in items:
        if flag is True:
            if inventory.get(item) is None:
                inventory[item] = 1
            else:
                inventory[item] += 1
        elif flag is False:
            if inventory.get(item) is not None:
                if inventory[item] > 0:
                    inventory[item] -= 1

    return inventory


def create_inventory(items: list):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}

    new = loop(inventory, items, True)

    return new


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    new = loop(inventory, items, True)

    return new


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    new = loop(inventory, items, False)

    return new


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if inventory.get(item) is not None:
        inventory.pop(item)
    return inventory


def list_inventory(inventory: dict) -> list[tuple]:
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    list_of_inventory = []

    for key in inventory:
        if inventory[key] > 0:
            list_of_inventory.append((key, inventory[key]))

    return sorted(list_of_inventory)
