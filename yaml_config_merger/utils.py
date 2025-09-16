from pathlib import Path
from typing import Union
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

__all__ = ['load_config', 'dump_config']

def load_config(path:Union[str,Path], **kwargs) -> dict:
    try:
        with open(path, 'r') as fp:
            return yaml.load(fp, Loader=Loader, **kwargs)
    except Exception:
        raise

def dump_config(path:Union[str,Path], config:dict, ensure_ascii=True, **kwargs) -> None:
    try:
        with open(path, 'w') as fp:
            yaml.dump(config, fp, Dumper=Dumper, allow_unicode=(not ensure_ascii), **kwargs)
    except Exception:
        raise