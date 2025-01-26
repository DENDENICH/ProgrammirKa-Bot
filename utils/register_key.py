import string
import random


class Keys:

    def __init__(self, path: str = 'keys'):
        self.path = path


    def _save_key(self, key: str) -> None:
        """Save key in file"""
        with open(self.path, mode="a", encoding='utf-8') as file:
            file.write(f"{key}\n")


    def generate_new_key(self, length: int = 16) -> str:
        """Generate new key and save it in file"""
        # Create set symbols and letters
        characters = string.ascii_letters + string.digits + string.punctuation
        # Генерируем строку заданной длины
        new_key = ''.join(random.choice(characters) for _ in range(length))
        self._save_key(key=new_key) # save key
        return new_key


    def get_all_keys(self) -> list[str]:
        """Read all keys from file"""
        with open(self.path, mode="r", encoding='utf-8') as file:
            return [key for key in file.read().split('\n')]


    def delete_key(self, key: str) -> None:
        keys = self.get_all_keys()
        keys.remove(key)
        with open(self.path, mode="w", encoding='utf-8') as file:
            file.write('\n'.join(keys))

keys = Keys()
