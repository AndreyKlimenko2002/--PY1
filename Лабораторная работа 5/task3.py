from random import randint

def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    random_numbers = []
    unique = []
    for _ in range(15):
        a = randint(-10, 10)
        while a in unique:
            a = randint(-10, 10)
        random_numbers.append(a)
        unique.append(a)
    return random_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
