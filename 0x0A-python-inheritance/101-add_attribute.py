#!/usr/bin/python3

def add_attribute(obj, attribute_name, attribute_value):
    """Add a new attribute to an object if it allows dynamic attributes.

    Args:
        obj (object): The object to which an attribute will be added.
        attribute_name (str): The name of the attribute to add.
        attribute_value (any): The value to assign to the attribute.

    Raises:
        TypeError: If the object does not support dynamic attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute_name, attribute_value)
