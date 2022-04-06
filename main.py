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
    answers = []
    user_input = input()
    while True:
        if user_input == 'exit':
            break
        words = user_input.split(' ')
        if words[0]=='put':
            key = words[1]
            values = getKeyValues(words, 2)
            answers.append(cache.put(key, values))
        elif words[0]=='get':
            key = words[1]
            answers.append(cache.get(key))
        elif words[0] == 'keys':
            answers.append(cache.keys())
            
        elif words[0] == 'search':
            key = words[1]
            value = getKeyValues(words, 1)
            answers.append(cache.search(key, value[key]))
            
        elif words[0] == 'delete':
            key = words[1]
            answers.append(cache.delete(key))
        user_input = input()
    for answer in answers:
        if answer !=None:
            print(answer)

if __name__ == '__main__':
    main()

