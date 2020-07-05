from CLI_MVC import terminal
from CLI_MVC import widgets
from CLI_MVC import models as mvcModels

from render import debug
from render import main
import models


def Render(model: models.Model):
    rows, cols = terminal.get_max_row_col()

    if model.mode == 0:
        debug.render(model, rows, cols)
    else:
        main.render(model, rows, cols)


def _render_view(model: models.Model, rows: int, cols: int):
    widgets.text_widget(
        mvcModels.Area(
            rows,
            cols,
            ),
        "Main"
    )


def _render_debug(model: models.Model, rows: int, cols: int):
    widgets.list_widget(
        mvcModels.Area(
            rows,
            cols,
            ),
        json.dumps(asdict(model), indent=2).split('\n'),
        list_offsset=model.debug_offset
        )

