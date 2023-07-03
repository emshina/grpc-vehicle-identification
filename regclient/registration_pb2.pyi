from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataEntry(_message.Message):
    __slots__ = ["Number_plate", "email", "id"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_PLATE_FIELD_NUMBER: _ClassVar[int]
    Number_plate: str
    email: str
    id: int
    def __init__(self, Number_plate: _Optional[str] = ..., email: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ["Number_plate"]
    NUMBER_PLATE_FIELD_NUMBER: _ClassVar[int]
    Number_plate: str
    def __init__(self, Number_plate: _Optional[str] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ["error", "success"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error: str
    success: bool
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...

class FetchRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FetchResponse(_message.Message):
    __slots__ = ["data_entries"]
    DATA_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    data_entries: _containers.RepeatedCompositeFieldContainer[DataEntry]
    def __init__(self, data_entries: _Optional[_Iterable[_Union[DataEntry, _Mapping]]] = ...) -> None: ...

class InsertRequest(_message.Message):
    __slots__ = ["Number_plate", "email", "id"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_PLATE_FIELD_NUMBER: _ClassVar[int]
    Number_plate: str
    email: str
    id: int
    def __init__(self, Number_plate: _Optional[str] = ..., email: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class InsertResponse(_message.Message):
    __slots__ = ["error", "success"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error: str
    success: bool
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ["Number_plate", "condition", "email", "id"]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_PLATE_FIELD_NUMBER: _ClassVar[int]
    Number_plate: str
    condition: str
    email: str
    id: int
    def __init__(self, Number_plate: _Optional[str] = ..., email: _Optional[str] = ..., id: _Optional[int] = ..., condition: _Optional[str] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ["error", "success"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error: str
    success: bool
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...
