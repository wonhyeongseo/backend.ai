from typing import Sequence, Union

from .base import Dict, Key, Trafaret

class KeysSubset(Key):
    def __init__(self, *keys: Sequence[str]): ...
    def __call__(self, data): ...

def subdict(name: str, *keys: Sequence[Union[str, Key]], trafaret: Trafaret) -> Dict: ...
def xor_key(first, second, trafaret: Trafaret): ...
def confirm_key(name, confirm_name, trafaret: Trafaret): ...
