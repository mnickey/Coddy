class CustomList:
    def __init__(self, items=None):
        # TODO: Initialize the items attribute
        # If items is None, set self.items to an empty list
        # Otherwise, convert items to a list using list(items)
        pass
    
    def __len__(self):
        # TODO: Return the length of self.items using len()
        pass
    
    def __getitem__(self, index):
        # TODO: Return the item at the specified index from self.items
        pass
    
    def __setitem__(self, index, value):
        # TODO: Set the value at the specified index in self.items
        pass
    
    def __str__(self):
        # TODO: Return a string representation of self.items
        # This should look like a regular Python list: "[1, 2, 3]"
        pass
    
    def __repr__(self):
        # TODO: Return a string that, when evaluated, would recreate this object
        # Format: "CustomList([1, 2, 3])"
        pass
    
    def __add__(self, other):
        # TODO: Implement addition with another CustomList or regular list
        # If other is a CustomList, add self.items and other.items
        # Otherwise, add self.items and list(other)
        # Return a new CustomList containing the combined items
        pass
    
    def __iter__(self):
        # TODO: Return an iterator for self.items
        # Hint: Use the built-in iter() function
        pass
    
    def __contains__(self, item):
        # TODO: Return True if item is in self.items, False otherwise
        pass
    
    def append(self, item):
        # TODO: Add the item to the end of self.items
        pass
    
    def pop(self):
        # TODO: Remove and return the last item from self.items
        pass
    
    def clear(self):
        # TODO: Remove all items from self.items
        pass
