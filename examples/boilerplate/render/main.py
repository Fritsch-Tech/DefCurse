import models

from CLI_MVC import widgets
from CLI_MVC import style
from CLI_MVC import models as mvcModels

def render(model: models.Model, rows: int, cols: int):
    areas = [
        mvcModels.Area(
            int(rows/2),
            int(cols/2),
        ),
        mvcModels.Area(
            int(rows/2),
            int(cols/2),
            int(rows/2)
        ),
        mvcModels.Area(
            int(rows/2),
            int(cols/2),
            0,
            int(cols/2)
        ),
        mvcModels.Area(
            int(rows/2),
            int(cols/2),
            int(rows/2),
            int(cols/2),
        ),
    ]
    a = widgets.labeled_box_widget(
        areas[0],
        "Main 0"
    )
    widgets.labeled_box_widget(
        areas[1],
        "Main 1"
    )
    widgets.labeled_box_widget(
        areas[2],
        "Main 2"
    )
    widgets.labeled_box_widget(
        areas[3],
        "Main 3"
    )
    
    widgets.text_widget(
        a,
        style.inverse(
            "Hallo " + 
            style.bold("Welt ") + 
            " 4321"
            ) +
        " 1234"
        )