from DefCurse import box_borders
from DefCurse import style
from DefCurse import helpers
from DefCurse import area
from DefCurse import terminal


from typing import List


# support line wrapping
def text_widget(area: area.Area,text:str) -> area.Area:
    terminal._add_str(
        area.height_offset, 
        area.width_offset,
        text
        )

    
def box_widget(area: area.Area,border_style:dir=box_borders.single) -> area.Area:
    """Draws a box around a specified area, then returns the area inside of the box

    Args:
        area (area.Area): Area to be boxed in
        border_style (dir, optional): The look of the border, deafults can be found in the box_boder.py file. The dir requires the following fields: 
        topLeft,topRight,bottomRight,bottomLeft,vertical,horizontal.Defaults to box_borders.single.

    Returns:
        area.Area: return the area inside of the box
    """
    # Top Line
    terminal._add_str(
        area.height_offset,
        area.width_offset,
        border_style["topLeft"]+border_style["horizontal"] *
        (area.width-2)+border_style["topRight"]
    )
    
    #Bottom Line
    terminal._add_str(
        area.height_offset+area.height-1,
        area.width_offset,
        border_style["bottomLeft"]+border_style["horizontal"] *
        (area.width-2)+border_style["bottomRight"]
    )
    
    #Side Lines
    for line_index in range(area.height-2):
        terminal._add_str(
            area.height_offset+line_index+1,
            area.width_offset,
            border_style["vertical"]
        )
        terminal._add_str(
            area.height_offset+line_index+1,
            area.width_offset+area.width-1,
            border_style["vertical"]
        )
        
    return area.Area(
        height=area.height-2,
        width=area.width-2,
        width_offset=area.width_offset+1,
        height_offset=area.height_offset+1,
    )

def labeled_box_widget(area: area.Area,border_style:dir=box_borders.single,label:str="") -> area.Area:
    nArea = box_widget(area,border_style)
    if label:
        terminal._add_str(area.height_offset, area.width_offset+1,label)
    return nArea
    

def list_widget(
    area:  area.Area,
    list: list,
    selected_item: str = None,
    list_offsset: int = 0,
) -> area.Area:

    for idx, entry in enumerate(list[list_offsset:area.height+list_offsset]):
        if entry == selected_item:
            terminal._add_str(area.height_offset+idx, area.width_offset, style.inverse(helpers.shorten_str_pure(entry,width)))
        else:
            terminal._add_str(area.height_offset+idx, area.width_offset, helpers.shorten_str_pure(entry,area.width))
    
    return area