class Attributes:

    def __init__(self, key):
        self.key = key
        self.values = {}

    def __str__(self):
        return ', '.join([str(k)+":"+str(v) for (k,v) in self.values.items()])

    def add_values(self, values):
        if self.values:
            newValues = {}
            for (oldKey, newKey),(oldValue, newValue) in zip(self.values.items(), values.items()):
                if type(oldValue) != type(newValue):
                    return 'Data type Error'
                else:
                    newValues[newKey] = newValue
            self.values = newValues
            return None
        else:
            self.values = values

    def search(self, key, value):
        if key in self.values.keys() and self.values[key] == value:
            return True
        return False