import yaml

__config = None


def config():
    """Read the configuration of the environment in which it is executed"""

    global __config
    if not __config:
        with open('config.yaml', mode='r', encoding='utf-8') as f:
            __config = yaml.safe_load(f)

    return __config