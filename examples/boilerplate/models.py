from dataclasses import dataclass
from typing import List


@dataclass
class Model:
    mode:               int = 1 # 0 = debug
                                # 1 = main
    debug_offset:       int = 0
    exit:               bool = False