from DefCurse import main
from DefCurse import widgets
from DefCurse import area
from DefCurse import terminal
from DefCurse import helpers


from dataclasses import dataclass, replace, asdict
from typing import List

import os
import json


@dataclass
class Model:
    last_key:   str = ""
    exit:       bool = False


def view(model: Model) -> None:
    widgets.text_widget(area.Area(1,10,0),model.last_key.encode('unicode_escape'))
    widgets.text_widget(area.Area(1,10,1),model.last_key)
    widgets.text_widget(area.Area(1,10,2),list(map(ord,list(model.last_key))))
    widgets.list_widget(
        widgets.box_widget(
            area.Area(
                6,
                45,
                5,
                0
            )
        ),
        helpers.add_line_numbers(json.dumps(asdict(model), indent=2).split("\n"))
    )


def handler(model: Model, event: str) -> Model:
    return replace(model,last_key=event)


def exit_condition(model: Model) -> bool:
    return model.exit


if __name__ == '__main__':
    main.wrapper(
        Model(),
        view,
        handler,
        exit_condition,
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "crashlogs",   
        )
    )