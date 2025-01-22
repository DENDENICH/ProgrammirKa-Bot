import string
import random


def generate_key(length: int = 16) -> str:
    # Создаем набор символов: буквы и цифры
    characters = string.ascii_letters + string.digits + string.punctuation
    # Генерируем строку заданной длины
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def save_key(
        key: str,
        path: str = "keys"
        ) -> None:
    """Save key in file"""
    with open("keys", mode="w", encoding='utf-8') as file:
        file.write(f"{key}")
    

def read_key(path: str = "keys") -> str:
    """Delete key from file

    Args:
        path (str, optional): _description_. Defaults to "keys".
    """
    with open(path, mode="r", encoding='utf-8') as file:
        return file.read()



def delete_key(path: str = "keys") -> None:
    """Delete key from file

    Args:
        path (str, optional): _description_. Defaults to "keys".
    """
    with open(path, mode="w", encoding="utf-8") as file:
        file.write()
