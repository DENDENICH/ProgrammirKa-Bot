from environs import Env


env = Env
env.read_env('.env')


class TGConfig:
    token: str = env('token')
    admin_id: int = int(env('admin_id'))


tg_config = TGConfig()
