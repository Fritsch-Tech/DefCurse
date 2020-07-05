from CLI_MVC import box_borders
from CLI_MVC import style
from CLI_MVC import helpers
from CLI_MVC import models
from CLI_MVC import terminal


from typing import List

def add_line_numbers(list: List[str]) -> List[str]:
    line_number_length = len(str(len(list))) + 2
    return [(str(idx)+": ").rjust(line_number_length)+e for idx, e in enumerate(list)]

# support line wrapping
def text_widget(area: models.Area,text:str) -> models.Area:
    terminal._add_str(
        area.height_offset, 
        area.width_offset,
        text
        )

    

def box_widget(area: models.Area) -> models.Area:
    borders: dir = box_borders.round
    # Top Line
    terminal._add_str(
        area.height_offset,
        area.width_offset,
        borders["topLeft"]+borders["horizontal"] *
        (area.width-2)+borders["topRight"]
    )
    terminal._add_str(
        area.height_offset+area.height-1,
        area.width_offset,
        borders["bottomLeft"]+borders["horizontal"] *
        (area.width-2)+borders["bottomRight"]
    )
    for line_index in range(area.height-2):
        terminal._add_str(
            area.height_offset+line_index+1,
            area.width_offset,
            borders["vertical"]
        )
        terminal._add_str(
            area.height_offset+line_index+1,
            area.width_offset+area.width-1,
            borders["vertical"]
        )
        
    return models.Area(
        height=area.height-2,
        width=area.width-2,
        width_offset=area.width_offset+1,
        height_offset=area.height_offset+1,
    )

def labeled_box_widget(area: models.Area,name:str) -> models.Area:
    nArea = box_widget(area)
    terminal._add_str(area.height_offset, area.width_offset+1,name)
    return nArea
    

def list_widget(
    area:  models.Area,
    list: list,
    selected_item: str = None,
    list_offsset: int = 0,
) -> models.Area:

    for idx, entry in enumerate(list[list_offsset:area.height+list_offsset]):
        if entry == selected_item:
            terminal._add_str(area.height_offset+idx, area.width_offset, style.inverse(helpers.shorten_str_pure(entry,width)))
        else:
            terminal._add_str(area.height_offset+idx, area.width_offset, helpers.shorten_str_pure(entry,area.width))
    
    return area