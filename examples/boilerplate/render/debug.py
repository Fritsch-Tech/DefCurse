from dataclasses import asdict
import json

from CLI_MVC import widgets
from CLI_MVC import models as mvcModels

import models


def render(model: models.Model, rows: int, cols: int):
    widgets.list_widget(
        widgets.labeled_box_widget(
            mvcModels.Area(
            rows,
            cols,
            ),
            "Debug"
         ),
        json.dumps(asdict(model), indent=2).split('\n'),
        list_offsset=model.debug_offset
        )