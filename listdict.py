class ListDictionary:
    def __init__(self):
        # implement the constructor
        self.lst_keys = []
        self.lst_values = []

    def insert(self, key, value):
        # Implement the insert() method
        index = 0

        # Go through the list and search for a matching key
        for i in range(len(self.lst_keys)):
            if self.lst_keys[i] == key:
                # Found a match, update value
                # print("Found a match")
                self.lst_values[i] = value
                return True
            index += 1

        # no match found, return FALSE
        self.lst_keys.append(key)
        self.lst_values.append(value)
        return False

    def remove(self, key):
        index = 0

        # Go through the list and search for a matching key
        for i in range(len(self.lst_keys)):
            if self.lst_keys[i] == key:
                # Found a match, update value
                # print("Found a match")
                self.lst_values.pop(index)
                return True
            index += 1
            
        # No key found
        return False
    
    def contains(self, key):
        if key in self.lst_keys:
            return True
        else:
            return False
        
    def lookup(self, key):
        index = 0

        # Go through the list and search for a matching key
        for i in range(len(self.lst_keys)):
            if self.lst_keys[i] == key:
                # Found a match, update value
                # print("Found a match")
                return self.lst_values[i]
            index += 1
        return None
    
    def get_keys(self): 
        return self.lst_keys
    
    def get_values(self):
        return self.lst_values
    
    def size(self):
        return len(self.lst_keys)
        
