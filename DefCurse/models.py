from dataclasses import dataclass

@dataclass
class Area:
    height: int
    width: int
    height_offset: int = 0
    width_offset: int = 0