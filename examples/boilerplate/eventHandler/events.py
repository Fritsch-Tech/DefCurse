from dataclasses import replace

import models
        
        
def _quit(model: models.Model, event: str):
    return replace(model, exit=True)


def _switch_modes(model: models.Model, event: str):
    return replace(model, mode=int(not bool(model.mode)))


def _default(model: models.Model, event: str):
    return model

