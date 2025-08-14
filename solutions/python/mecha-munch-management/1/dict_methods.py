"""Functions to manage a user's shopping cart items."""

from typing import Dict, Iterable, List, Tuple, Any


def add_item(current_cart: Dict[str, int], items_to_add: Iterable[str]) -> Dict[str, int]:
    """
    Add items to a shopping cart.

    Parameters:
        current_cart: dict mapping item -> quantity
        items_to_add: iterable of items to add

    Returns:
        Updated cart dictionary
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes: Iterable[str]) -> Dict[str, int]:
    """
    Create a user cart from an iterable of notes (items).

    Parameters:
        notes: iterable of item names

    Returns:
        Cart dictionary with item counts
    """
    cart = {}
    for item in notes:
        cart[item] = cart.get(item, 0) + 1
    return cart


def update_recipes(ideas: Dict[str, Dict[str, int]], recipe_updates: Iterable[Tuple[str, Dict[str, int]]]) -> Dict[str, Dict[str, int]]:
    """
    Update a recipes dictionary with new recipe info.

    Parameters:
        ideas: existing recipe dictionary (recipe -> ingredient dict)
        recipe_updates: iterable of tuples (recipe_name, ingredient dict)

    Returns:
        Updated recipes dictionary
    """
    for key, value in recipe_updates:
        ideas[key] = value
    return ideas


def sort_entries(cart: Dict[str, int]) -> Dict[str, int]:
    """
    Sort a user's shopping cart alphabetically by item name.

    Parameters:
        cart: dictionary of item -> quantity

    Returns:
        Sorted dictionary
    """
    return dict(sorted(cart.items(), key=lambda x: x[0]))


def send_to_store(cart: Dict[str, int], aisle_mapping: Dict[str, List[Any]]) -> Dict[str, List[Any]]:
    """
    Combine user cart with aisle and refrigeration information for store fulfillment.

    Items are returned in reverse alphabetical order.

    Parameters:
        cart: user's shopping cart (item -> quantity)
        aisle_mapping: mapping of item -> [aisle, refrigerated_flag]

    Returns:
        dict mapping item -> [quantity, aisle, refrigerated_flag], sorted in reverse alphabetical order.
        Items not in aisle_mapping are ignored.
    """
    # Only include items that exist in aisle_mapping
    combined = {
        item: [cart[item], aisle_mapping[item][0], aisle_mapping[item][1]]
        for item in cart
        if item in aisle_mapping
    }

    # Sort in reverse alphabetical order
    return dict(sorted(combined.items(), key=lambda x: x[0], reverse=True))


def update_store_inventory(fulfillment_cart: Dict[str, List[Any]], store_inventory: Dict[str, List[Any]]) -> Dict[str, List[Any]]:
    """
    Update store inventory levels based on a fulfillment cart.

    Parameters:
        fulfillment_cart: dict of item -> [quantity, aisle, refrigerated_flag]
        store_inventory: dict of item -> [current_quantity, aisle, refrigerated_flag]

    Returns:
        Updated store inventory with quantities reduced, or 'Out of Stock' if quantity goes below 0.
    """
    for item, (qty, _, _) in fulfillment_cart.items():
        if item in store_inventory:
            new_qty = store_inventory[item][0] - qty
            if new_qty <= 0:
                store_inventory[item][0] = "Out of Stock"
            else:
                store_inventory[item][0] = new_qty
    return store_inventory
