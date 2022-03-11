from typing import List, Union
from pydantic import BaseModel


class LoadRequest(BaseModel):
    chunk: List[Union[int, None]]


class CheckRequest(BaseModel):
    pattern: List[Union[int, None]]


class CheckResponse(BaseModel):
    exists: bool
