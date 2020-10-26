from DefCurse import terminal
from DefCurse import widgets

from render import debug
from render import main
import models


def Render(model: models.Model):
    rows, cols = terminal.get_max_row_col()

    if model.mode == 0:
        debug.render(model, rows, cols)
    else:
        main.render(model, rows, cols)