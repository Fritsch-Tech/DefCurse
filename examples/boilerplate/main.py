#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from dataclasses import replace, asdict

from DefCurse import main

from models import Model
from render.render import Render
from eventHandler.eventHandler import EventHandler


def exit_condition(model: Model) -> bool:
    if model.exit:
        return False
    else:
        return True


if __name__ == '__main__':
    main.wrapper(
        Model(),
        Render,
        EventHandler,
        exit_condition,
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "crashlogs",   
        )
    )