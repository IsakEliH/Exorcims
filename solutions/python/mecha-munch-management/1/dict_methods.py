"""Functions to manage a users shopping cart items."""


def add_item(current_cart: dict, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        # If the item is not in current cart
        if current_cart.get(item) is None:
            current_cart.setdefault(item, 1)
        # If the item is in the cart add to the count
        else:
            current_cart[item] += 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    shopping_cart: dict = {}
    sc = shopping_cart.fromkeys(notes, 1)
    return sc


def update_recipes(ideas: dict, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    # Recipe_update gives a tuple, so extract and create a temp dict
    for recipe in recipe_updates:
        temp_dict = {recipe[0]: recipe[1]}
        ideas.update(temp_dict)

    return ideas


def sort_entries(cart: dict):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart: dict, aisle_mapping: dict):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    updated_cart = {}
    for key in aisle_mapping:
        value: list = aisle_mapping[key]

        num_value = cart.get(key)
        if num_value is None:
            continue

        new_list: list = [num_value] + value

        updated_cart[key] = new_list

    return dict(sorted(updated_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart: dict, store_inventory: dict):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    updated_inventory: dict = {}
    for key in store_inventory:
        value = store_inventory[key]

        cart_key = fulfillment_cart.get(key)
        num = value[0]

        if cart_key is not None:
            num = value[0] - cart_key[0]
            if num <= 0:
                num = "Out of Stock"

        u_value = value
        u_value[0] = num
        updated_inventory.setdefault(key, u_value)

    return updated_inventory
