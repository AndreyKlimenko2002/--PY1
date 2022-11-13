from random import sample

def get_random_password(p = 8) -> str:
    ...  # TODO написать функцию генерации случайных паролей
    a = "qwertyuiopasdfghjklzxcvbnm"
    letters = [a for a in a] # нижний регистр
    letters_ = [a.upper() for a in a] # верхний регистр
    numbers = [str(n) for n in range (10)]
    combination = letters + letters_ + numbers
    password = "".join(sample(combination, p))
    return password

print(get_random_password())
