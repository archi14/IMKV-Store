from attributes import Attributes
class Cache:
    cache = dict()

    def get(self, key):
        if key not in self.cache.keys():
            print(f'No Entry found for {key}')
            return
        print(str(self.cache[key]))

    def search(self, attributeKey, attributeValue):
        returnKeys = []
        for key in self.cache.keys():
            if self.cache[key].search(attributeKey, attributeValue):
                returnKeys.append(key)
        print(','.join(returnKeys))


    def put(self, key, values):
        if key not in self.cache.keys():
            self.cache[key] = Attributes(key)
        self.cache[key].add_values(values)
    
    def delete(self, key):
        self.cache.pop(key)

    def keys(self):
        returnKeys = []
        for key in self.cache.keys():
            returnKeys.append(key)
        print(','.join(returnKeys))
    

    