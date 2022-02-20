
nested_list = [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None],]


class FlatIterator:
    def __init__(self, list_of_lists):
        self.lst = list_of_lists
        self.cursor = -1
        self.list_len = len(self.lst)

    def __iter__(self):
        self.cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        if self.nest_cursor == len(self.lst[self.cursor]):
          iter(self)
        if self.cursor == self.list_len:
          raise StopIteration
        self.nest_cursor += 1
        return self.lst[self.cursor][self.nest_cursor - 1]

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        if type(item) == bool:
            print(item)
        elif type(item) == int:
            print(item)
        elif item is None:
            print(item)
        else:
            print(f"'{item}'")
    print()
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)