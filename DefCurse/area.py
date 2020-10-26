from dataclasses import dataclass
from typing import Callable, Generic, Any
from functools import partial

@dataclass
class Area:
    height: int
    width: int
    height_offset: int = 0
    width_offset: int = 0
    

def _unfold(f:Callable[[Any], Any],seed:Any,count:int)->[]:
    """Generates a list where each entry is the the retrun value of the given function and the previous value/seed. 

    Args:
        f (Callable[[Any], Any]): Applied Function.
        seed (Any): Starting list value.
        count (int): Length of the resulting list -1.

    Returns:
        []: Resulting List
    """
    if count == 0:
        return [seed]
    
    return [seed]+_unfold(f,f(seed),count-1)


def translate(area:Area,width:int=0,height:int=0)->Area:
    """Generates a new Area with a relative offset to the original.

    Args:
        area (Area): Original area
        width (int, optional): Added width offset. Defaults to 0.
        height (int, optional): Added height offset. Defaults to 0.

    Returns:
        Area: Area in new location
    """
    return Area(
        area.height,
        area.width,
        area.height_offset+height,
        area.width_offset+width
    )
    

def translate_clone(area:Area,count:int,width:int=0,height:int=0)->[Area]:
    """Generate clones of the input list each with a relative offset to the previous one.

    Args:
        area (Area): Original area
        count (int): number of additional areas
        width (int, optional): Relative width offset. Defaults to 0.
        height (int, optional): Relative height offset. Defaults to 0.

    Returns:
        [Area]: List of generated Areas, Index 0 is the original
    """
    return _unfold(
        partial(translate,width=width,height=height)
        ,area,count
    )
