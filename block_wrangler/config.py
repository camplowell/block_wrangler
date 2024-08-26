from dataclasses import dataclass, asdict
from typing import Self, dataclass_transform

@dataclass_transform(kw_only_default=True)
class ConfigMeta(type):
    def __new__(cls, name, bases, dct):
        dct['__specified_fields__'] = set()
        instance = super().__new__(cls, name, bases, dct)
        dataclass(kw_only=True)(instance)
        base_init = instance.__init__
        def __init__(self, **kwargs):
            self.__specified_fields__ = {k for k in self.__dataclass_fields__ if k in kwargs}
            base_init(self, **kwargs)
        setattr(instance, '__init__', __init__)

        return instance

class Configuration(metaclass=ConfigMeta):
    def override(self, **kwargs):
            my_fields = asdict(self)
            for k, v in kwargs.items():
                if k in my_fields:
                    my_fields[k] = v
            return type(self)(**my_fields)
    def __or__(self, other:'Configuration|dict') -> Self:
        """Fill in any unspecified fields with values from other"""
        if isinstance(other, dict):
            if not all(k in self.__dataclass_fields__ for k in other.keys()):
                raise KeyError(f'{type(self).__name__} has no field(s) {", ".join(k for k in other.keys() if k not in self.__dataclass_fields__)}')
        elif not isinstance(self, type(other)):
            raise TypeError('Cannot merge non-Config objects')
        else:
            other = asdict(other)
        specified = {k:v for k, v in asdict(self).items() if k in self.__specified_fields__} #type: ignore
        return type(self)(**(other | specified))