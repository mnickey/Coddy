class CustomList:
    def __init__(self, items=None):
        # TODO: Initialize the items attribute
        # If items is None, set self.items to an empty list
        # Otherwise, convert items to a list using list(items)
        if items == None:
            self.items = []
        else:
            self.items = list(items)
    
    def __len__(self):
        # TODO: Return the length of self.items using len()
        return len(self.items)
    
    def __getitem__(self, index):
        # TODO: Return the item at the specified index from self.items
        return self.items[index]
    
    def __setitem__(self, index, value):
        # TODO: Set the value at the specified index in self.items
        self.items[index] = value
    
    def __str__(self):
        # TODO: Return a string representation of self.items
        # This should look like a regular Python list: "[1, 2, 3]"
        return str(self.items)
    
    def __repr__(self):
        # TODO: Return a string that, when evaluated, would recreate this object
        # Format: "CustomList([1, 2, 3])"
        return f"CustomList({self.items})"
    
    def __add__(self, other):
        # TODO: Implement addition with another CustomList or regular list
        # If other is a CustomList, add self.items and other.items
        # Otherwise, add self.items and list(other)
        # Return a new CustomList containing the combined items
        if other == CustomList():
            combined_items = self.items + other.items
            return CustomList(combined_items)
        else:
            combined_items = self.items + list(other)
            return CustomList(combined_items)
    
    def __iter__(self):
        # TODO: Return an iterator for self.items
        # Hint: Use the built-in iter() function
        return iter(self.items)
    
    def __contains__(self, item):
        # TODO: Return True if item is in self.items, False otherwise
        if item in self.items:
            return True
        else:
            return False
    
    def append(self, item):
        # TODO: Add the item to the end of self.items
        self.items.append(item)
    
    def pop(self):
        # TODO: Remove and return the last item from self.items
        return self.items.pop()
    
    def clear(self):
        # TODO: Remove all items from self.items
        self.items.clear()
