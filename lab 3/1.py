def field(goods, *args):
    for item in goods:
        if len(args) == 1:
            # Если передан только один аргумент
            value = item.get(args[0])
            if value is not None:
                yield value #
        else:
            # Если передано несколько аргументов
            result = {arg: item.get(arg) for arg in args if item.get(arg) is not None}
            if result:
                yield result # возвращает из функции result

# Пример использования
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

# Генерация значений одного поля
for title in field(goods, 'title'):
    print(title)

# Генерация значений нескольких полей
for item in field(goods, 'title', 'price'):
    print(item)