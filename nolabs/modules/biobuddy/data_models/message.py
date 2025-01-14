from enum import Enum
from typing import Any, List, Union
from pydantic.dataclasses import dataclass


@dataclass
class File:
    name: str
    content: str


@dataclass
class RegularMessage:  # Should be completely the same as in api models
    content: str


@dataclass
class FunctionParam:  # Should be completely the same as in api models
    name: str
    value: Any = None


@dataclass
class FunctionCall:  # Should be completely the same as in api models
    function_name: str
    parameters: List[FunctionParam]

class MessageType(Enum):
    TEXT = "text"
    FUNCTIONS = "function"

@dataclass
class Message:  # Should be completely the same as in api models
    id: str
    role: str
    message: Union[RegularMessage, List[FunctionCall]]
    type: MessageType
