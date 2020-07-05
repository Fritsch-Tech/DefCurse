from CLI_MVC import blesses
from CLI_MVC import widgets
from CLI_MVC import models
from CLI_MVC import terminal

from dataclasses import dataclass, replace, asdict
from typing import List

import os
import json


@dataclass
class Model:
    last_key:   str = ""
    exit:       bool = False


def view(model: Model) -> None:
    widgets.text_widget(models.Area(1,10,0),model.last_key.encode('unicode_escape'))
    widgets.text_widget(models.Area(1,10,1),model.last_key)
    widgets.text_widget(models.Area(1,10,2),list(map(ord,list(model.last_key))))
    widgets.list_widget(
        widgets.box_widget(
            models.Area(
                6,
                30,
                5,
                0
            )
        ),
        widgets.add_line_numbers(json.dumps(asdict(model), indent=2).split("\n"))
    )


def handler(model: Model, event: str) -> Model:
    return replace(model,last_key=event)


def exit_condition(model: Model) -> bool:
    if model.exit:
        return False
    else:
        return True


if __name__ == '__main__':
    blesses.wrapper(
        Model(),
        view,
        handler,
        exit_condition,
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "crashlogs",   
        )
    )