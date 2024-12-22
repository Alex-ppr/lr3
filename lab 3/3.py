class Unique:
    def __init__(self, items, **kwargs):
        self.items = items
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self.iterator = iter(items)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self.iterator)
            # Приводим к нижнему регистру, если ignore_case=True
            key = item.lower() if self.ignore_case and isinstance(item, str) else item

            if key not in self.seen:
                self.seen.add(key)
                return item


# Пример использования
data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
unique_data1 = Unique(data1)
print(list(unique_data1))  # Вывод: [1, 2]

data2 = (x for x in range(1, 4))  # Генератор
unique_data2 = Unique(data2)
print(list(unique_data2))  # Вывод: [1, 2, 3]

data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
unique_data3 = Unique(data3)
print(list(unique_data3))  # Вывод: ['a', 'A', 'b', 'B']

unique_data4 = Unique(data3, ignore_case=True)
print(list(unique_data4))  # Вывод: ['a', 'b']