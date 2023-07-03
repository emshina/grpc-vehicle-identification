from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Charges_entries(_message.Message):
    __slots__ = ["Number_plate", "charges", "date", "id"]
    CHARGES_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_PLATE_FIELD_NUMBER: _ClassVar[int]
    Number_plate: str
    charges: str
    date: str
    id: int
    def __init__(self, id: _Optional[int] = ..., Number_plate: _Optional[str] = ..., charges: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class DataNTSAEntry(_message.Message):
    __slots__ = ["Number_plate", "date", "email", "id"]
    DATE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_PLATE_FIELD_NUMBER: _ClassVar[int]
    Number_plate: str
    date: str
    email: str
    id: int
    def __init__(self, Number_plate: _Optional[str] = ..., email: _Optional[str] = ..., id: _Optional[int] = ..., date: _Optional[str] = ...) -> None: ...

class DeleteChargesRequest(_message.Message):
    __slots__ = ["ID", "police_code"]
    ID: int
    ID_FIELD_NUMBER: _ClassVar[int]
    POLICE_CODE_FIELD_NUMBER: _ClassVar[int]
    police_code: int
    def __init__(self, ID: _Optional[int] = ..., police_code: _Optional[int] = ...) -> None: ...

class DeleteChargesResponse(_message.Message):
    __slots__ = ["error", "success"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error: str
    success: bool
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...

class FetchNTSARequest(_message.Message):
    __slots__ = ["Number_plate"]
    NUMBER_PLATE_FIELD_NUMBER: _ClassVar[int]
    Number_plate: str
    def __init__(self, Number_plate: _Optional[str] = ...) -> None: ...

class FetchNTSAResponse(_message.Message):
    __slots__ = ["data_entries"]
    DATA_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    data_entries: _containers.RepeatedCompositeFieldContainer[DataNTSAEntry]
    def __init__(self, data_entries: _Optional[_Iterable[_Union[DataNTSAEntry, _Mapping]]] = ...) -> None: ...

class FetchchargesRequest(_message.Message):
    __slots__ = ["Police_station_code_id"]
    POLICE_STATION_CODE_ID_FIELD_NUMBER: _ClassVar[int]
    Police_station_code_id: int
    def __init__(self, Police_station_code_id: _Optional[int] = ...) -> None: ...

class FetchchargesResponse(_message.Message):
    __slots__ = ["Charges_entries"]
    CHARGES_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    Charges_entries: _containers.RepeatedCompositeFieldContainer[Charges_entries]
    def __init__(self, Charges_entries: _Optional[_Iterable[_Union[Charges_entries, _Mapping]]] = ...) -> None: ...

class InsertChargesRequest(_message.Message):
    __slots__ = ["Number_plate", "Police_station_code_id", "charges"]
    CHARGES_FIELD_NUMBER: _ClassVar[int]
    NUMBER_PLATE_FIELD_NUMBER: _ClassVar[int]
    Number_plate: str
    POLICE_STATION_CODE_ID_FIELD_NUMBER: _ClassVar[int]
    Police_station_code_id: int
    charges: str
    def __init__(self, Number_plate: _Optional[str] = ..., charges: _Optional[str] = ..., Police_station_code_id: _Optional[int] = ...) -> None: ...

class InsertChargesResponse(_message.Message):
    __slots__ = ["error", "success"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    error: str
    success: bool
    def __init__(self, success: bool = ..., error: _Optional[str] = ...) -> None: ...

class PolicestationRequest(_message.Message):
    __slots__ = ["Police_station_code"]
    POLICE_STATION_CODE_FIELD_NUMBER: _ClassVar[int]
    Police_station_code: int
    def __init__(self, Police_station_code: _Optional[int] = ...) -> None: ...

class PolicestationResponse(_message.Message):
    __slots__ = ["station_entries"]
    STATION_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    station_entries: _containers.RepeatedCompositeFieldContainer[Station_entries]
    def __init__(self, station_entries: _Optional[_Iterable[_Union[Station_entries, _Mapping]]] = ...) -> None: ...

class Station_entries(_message.Message):
    __slots__ = ["Police_station_code", "station_name"]
    POLICE_STATION_CODE_FIELD_NUMBER: _ClassVar[int]
    Police_station_code: int
    STATION_NAME_FIELD_NUMBER: _ClassVar[int]
    station_name: str
    def __init__(self, station_name: _Optional[str] = ..., Police_station_code: _Optional[int] = ...) -> None: ...
