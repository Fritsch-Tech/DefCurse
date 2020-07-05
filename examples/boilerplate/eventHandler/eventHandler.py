from dataclasses import replace

import models
from eventHandler import debug
from eventHandler import main


def _invalide_mode(model: models.Model, event: str):
    replace(model, mode=1)


def EventHandler(model: models.Model, event: str):
    modes = {
        "0": debug._handler,
        "1": main._handler,
    }
    return modes.get(str(model.mode), _invalide_mode)(model, event)
