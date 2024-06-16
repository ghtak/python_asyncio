from dataclasses import dataclass


@dataclass
class Header:
    id: int
    size: int
    type: int
