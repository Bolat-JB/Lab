def camel_to_snake(camel_case):
    snake_case = ''
    for i in camel_case:
        if i.isupper():
            snake_case += '_' + i.lower()
        else:
            snake_case += i
    return snake_case.lstrip('_')

camel_str = input()

snake_str = camel_to_snake(camel_str)

print(snake_str)
