from dataclasses import replace

from eventHandler.events import _quit, _switch_modes, _default
import models
        
    
def _debug_up(model: models.Model, event: str):
    return replace(model, debug_offset=max(model.debug_offset-1, 0))


def _debug_down(model: models.Model, event: str):
    return replace(model, debug_offset=min(
        model.debug_offset+1,
        model.debug_model_length-1
    ))


def _handler(model: models.Model, event: str):
    events = {
        "q": _quit,
        "d":_switch_modes,
        "w": _debug_up,
        "s": _debug_down,
        "[A": _debug_up,
        "[B": _debug_down,
    }
    return events.get(event, _default)(model, event)
