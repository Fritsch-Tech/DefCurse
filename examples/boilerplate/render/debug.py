from dataclasses import asdict
import json

from DefCurse import widgets
from DefCurse import area
 
import models


def render(model: models.Model, rows: int, cols: int):
    widgets.list_widget(
        widgets.labeled_box_widget(
            area.Area(
            rows,
            cols,
            ),
            "Debug"
         ),
        json.dumps(asdict(model), indent=2).split('\n'),
        list_offsset=model.debug_offset
        )