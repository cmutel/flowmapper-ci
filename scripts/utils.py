import json
from pathlib import Path
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

def read_flowlist(filepath: Path):
    with open(filepath, 'r') as fs:
        result = json.load(fs)
    return result
