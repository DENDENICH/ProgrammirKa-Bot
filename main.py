import re

#from config import tg_config, bot, dp


def main() -> None:
    id = re.search( # TODO: проверить работу данного метода
        pattern=f"[1-9]+",
        string="fer_-23451"
        )
    
    id2 = re.findall( # TODO: проверить работу данного метода
        pattern=f"[1-9]+",
        string="fer_-23451"
        )
    print(int(id.group()))
    print(str(id))
    print(type(*id2))


    # TODO: инициализация и регистрация роутеров

main()