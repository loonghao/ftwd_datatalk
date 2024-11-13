# Import built-in modules
import os.path
from pathlib import Path
import sys

# Import third-party modules
from entity_addict import entity_addict
import yaml


@entity_addict
def get_config(key, default=None):
    path = get_config_file()
    if not path.exists():
        data = {}
    else:
        with open(path, "rb") as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
    return data.get(key, default)


def this_root():
    try:
        sys.frozen
    except AttributeError:
        return Path(__file__).parent
    else:
        return Path(os.path.dirname(sys.executable))


def get_config_file():
    return this_root() / "config.yaml"
