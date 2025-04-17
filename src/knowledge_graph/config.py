import tomli

def load_config(path):
    with open(path, 'rb') as f:
        return tomli.load(f)
