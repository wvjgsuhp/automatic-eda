from typing import Any, Dict, List, TypeVar, TypedDict
from typing_extensions import NotRequired
import pandas as pd

T = TypeVar('T')

DataFrame = pd.DataFrame
Kwargs = Dict[str, Any]


class Data(TypedDict):
    location: str
    filetype: str
    kwargs: NotRequired[Kwargs]


class Source(TypedDict):
    data: Dict[str, Data]
    filetype: Dict[str, Kwargs]


FigureConfig = Dict[str, Dict[str, Kwargs]]


class ExtraColumn(TypedDict):
    name: str
    method: str
    columns: List[str]


ExtraColumns = List[ExtraColumn]


class Eda(TypedDict):
    simple: NotRequired[FigureConfig]
    extra_columns: NotRequired[ExtraColumns]


class Path(TypedDict):
    location: str


class Output(TypedDict):
    figure: Path
    log: Path
    other: Path


class Config(TypedDict):
    source: Source
    output: Output
    eda: Dict[str, Eda]
