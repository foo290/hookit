from typing import List, Any, Dict, Tuple, TypeVar, NamedTuple
import json
from src.core.errors import ImmutableObjectError


class EventPriority(NamedTuple):
    NORMAL: str = 'normal'
    HIGH: str = 'high'
    LOW: str = 'low'
    CRITICAL: str = 'critical'


class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls, *args, **kwargs)
        return cls._instances[cls]


class RegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)

        RegistryMeta.registry[name] = new_class

        return new_class


class Immutable:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        raise ImmutableObjectError(f"Trying to set: {key} to an immutable object")

    def __setitem__(self, key, value):
        raise ImmutableObjectError(f"Trying to set: {key} to an immutable object")

    def __str__(self):
        return f"<ImmutableObject-{self.__class__.__name__} at {hex(id(self))}>"

    def __repr__(self):
        return f"<ImmutableObject-{self.__class__.__name__} at {hex(id(self))}>"


class CustomDictBase:

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self[key]

    def __repr__(self):
        data = json.dumps({k: v for k, v in self.__dict__.items() if not k.startswith('_')})
        return f"<{self.__class__.__name__}Object - data: {data}>"

    def __str__(self):
        data = json.dumps({k: v for k, v in self.__dict__.items() if not k.startswith('_')})
        return f"<{self.__class__.__name__}Object - data: {data}>"


class WebhookEventBase:
    ...


class WebhookPayloadBase(CustomDictBase):

    @classmethod
    def from_payload(cls, payload: dict):
        obj = cls()
        for key, val in payload.items():
            obj[key] = val
        return obj


