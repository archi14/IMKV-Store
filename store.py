from attributes import Attributes
class Cache:
    cache = dict()

    def get(self, key):
        if key not in self.cache.keys():
            statement = f"No entry found for {key}"
            return statement
        return str(self.cache[key])

    def search(self, attributeKey, attributeValue):
        returnKeys = []
        for key in self.cache.keys():
            if self.cache[key].search(attributeKey, attributeValue):
                returnKeys.append(key)
        return ','.join(returnKeys)


    def put(self, key, values):
        if key not in self.cache.keys():
            self.cache[key] = Attributes(key)
        return self.cache[key].add_values(values)
    
    def delete(self, key):
        self.cache.pop(key)

    def keys(self):
        returnKeys = []
        for key in self.cache.keys():
            returnKeys.append(key)
        return ','.join(returnKeys)
    

    