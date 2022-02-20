
nested_list = [['a', ['b', ['c']],[['d', ['e']], 'f'],[1, 2, None],]]

def flat_generator(list_of_lists):
    for el in list_of_lists:
        if isinstance(el, list):
            yield from flat_generator(el)
        else:
            yield el

if __name__ == '__main__':
    for item in  flat_generator(nested_list):
        if type(item) == bool:
            print(item)
        elif type(item) == int:
            print(item)
        elif item is None:
            print(item)
        else:
            print(f"'{item}'")
    print()
    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)
