from dataclasses import replace

from eventHandler.events import _quit, _switch_modes, _default
import models
        
    
def _handler(model: models.Model, event: str):    
    events = {
        "q": _quit,
        "d":_switch_modes,

    }
    return events.get(event, _default)(model, event)

