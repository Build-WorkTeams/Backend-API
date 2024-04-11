from functools import lru_cache
from pathlib import Path
from decouple import config as decouple_config, Config, RepositoryEnv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"


@lru_cache
def get_config():
    if ENV_FILE.exists():
        return Config(RepositoryEnv(ENV_FILE))
    else:
        return decouple_config
    
config = get_config()