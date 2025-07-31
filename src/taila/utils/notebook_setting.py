from taila.utils.settings import Settings
from pathlib import Path

def get_nb_setting():
    env_path = Path("../.envs/dev.env")
    setting = Settings.from_env_file(env_path)
    return setting