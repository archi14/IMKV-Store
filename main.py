from store import Cache

def getKeyValues(words, index):
    values = {}
    while index<len(words):
        if words[index+1].isdigit():
            words[index+1] = int(words[index+1])
        else:
            try:
                words[index+1] = float(words[index+1])
            except:
                if words[index+1] == "true":
                    words[index+1] = True
                elif words[index+1] == "false":
                    words[index+1] = False
        values[words[index]] = words[index+1]
        index+=2
    return values

def main():
    cache = Cache()

    user_input = input()
    while True:
        if user_input == 'exit':
            break
        words = user_input.split(' ')
        if words[0]=='put':
            key = words[1]
            values = getKeyValues(words, 2)
            cache.put(key, values)
        elif words[0]=='get':
            key = words[1]
            cache.get(key)
        elif words[0] == 'keys':
            cache.keys()
            
        elif words[0] == 'search':
            key = words[1]
            value = getKeyValues(words, 1)
            cache.search(key, value[key])
            
        elif words[0] == 'delete':
            key = words[1]
            cache.delete(key)
        user_input = input()

if __name__ == '__main__':
    main()

